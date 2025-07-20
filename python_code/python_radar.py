import pygame
import serial
import threading
import math
import tkinter as tk
from tkinter import simpledialog, messagebox
import os

# ==== SETTINGS ====
SCREEN_SIZE = 700
CENTER = SCREEN_SIZE // 2
RADAR_RADIUS = 300
MAX_DISTANCE = 200
ALERT_THRESHOLD = 60  # cm
FPS = 30
# ==================

# Sound setup
try:
    pygame.mixer.init()
    alert_sound = pygame.mixer.Sound("ping.wav")
    has_sound = True
except:
    alert_sound = None
    has_sound = False

# Prompt COM port
root = tk.Tk()
root.withdraw()
SERIAL_PORT = simpledialog.askstring("COM Port", "Enter Arduino COM port (e.g., COM5):")
if not SERIAL_PORT:
    messagebox.showerror("Error", "No COM port selected.")
    exit()
BAUD_RATE = 9600

# Globals
angle = 0
distance = 0

def read_serial():
    global angle, distance
    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        while True:
            line = ser.readline().decode().strip()
            if ',' in line:
                try:
                    a, d = line.split(',')
                    angle = int(a)
                    distance = int(d)
                except:
                    continue
    except Exception as e:
        print("Serial Error:", e)

# Start background thread
threading.Thread(target=read_serial, daemon=True).start()

# ======== Pygame Setup ========
pygame.init()
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("🛰 EchoSweep-360 | Radar Scanner")
clock = pygame.time.Clock()
font = pygame.font.SysFont("consolas", 20)
label_font = pygame.font.SysFont("consolas", 26, bold=True)

def draw_grid():
    screen.fill((0, 0, 0))
    green = (0, 255, 0)

    for r in range(50, RADAR_RADIUS+1, 50):
        pygame.draw.circle(screen, green, (CENTER, CENTER), r, 1)

    pygame.draw.line(screen, green, (CENTER, 0), (CENTER, SCREEN_SIZE), 1)
    pygame.draw.line(screen, green, (0, CENTER), (SCREEN_SIZE, CENTER), 1)

    for deg in range(0, 181, 30):
        rad = math.radians(deg)
        x = CENTER + (RADAR_RADIUS + 30) * math.cos(rad)
        y = CENTER - (RADAR_RADIUS + 30) * math.sin(rad)
        label = font.render(f"{deg}°", True, green)
        screen.blit(label, (x - 15, y - 10))

def draw_sweep(angle, dist_cm):
    dist_cm = min(dist_cm, MAX_DISTANCE)
    r = (dist_cm / MAX_DISTANCE) * RADAR_RADIUS
    rad = math.radians(angle)

    dot_x = CENTER + r * math.cos(rad)
    dot_y = CENTER - r * math.sin(rad)
    line_x = CENTER + RADAR_RADIUS * math.cos(rad)
    line_y = CENTER - RADAR_RADIUS * math.sin(rad)

    pygame.draw.line(screen, (0, 255, 0), (CENTER, CENTER), (line_x, line_y), 2)
    pygame.draw.circle(screen, (255, 0, 0), (int(dot_x), int(dot_y)), 6)

    # Detection note
    if dist_cm < ALERT_THRESHOLD:
        alert_label = label_font.render("⚠️ Object Detected!", True, (255, 50, 50))
        screen.blit(alert_label, (CENTER - 120, SCREEN_SIZE - 60))
        if has_sound:
            alert_sound.play()

def draw_buttons():
    pygame.draw.rect(screen, (70, 70, 70), (10, 10, 30, 30))  # Minimize
    pygame.draw.rect(screen, (200, 0, 0), (50, 10, 30, 30))   # Exit
    pygame.draw.line(screen, (255, 255, 255), (55, 15), (75, 35), 2)
    pygame.draw.line(screen, (255, 255, 255), (75, 15), (55, 35), 2)
    pygame.draw.line(screen, (255, 255, 255), (15, 25), (35, 25), 2)

# ======== Main App ========
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if 10 <= x <= 40 and 10 <= y <= 40:
                pygame.display.iconify()
            elif 50 <= x <= 80 and 10 <= y <= 40:
                running = False

    draw_grid()
    draw_sweep(angle, distance)
    draw_buttons()
    pygame.display.flip()

pygame.quit()
