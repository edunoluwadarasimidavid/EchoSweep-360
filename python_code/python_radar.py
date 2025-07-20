import pygame
import serial
import math
import threading

# ======= SETTINGS =======
SCREEN_SIZE = 600
CENTER = SCREEN_SIZE // 2
MAX_DISTANCE_CM = 200
RADAR_RADIUS = 250
SERIAL_PORT = 'COM5'  # 🔁 Change this to your Arduino port
BAUD_RATE = 9600
# ========================

# Global data
angle = 0
distance = 0

# ====== Serial Thread ======
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
                    continue  # Skip bad data
    except Exception as e:
        print("⚠️ Serial Error:", e)

# Start reading serial in background
threading.Thread(target=read_serial, daemon=True).start()

# ====== Pygame Setup ======
pygame.init()
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("🛰 Arduino Radar - Python Version")
clock = pygame.time.Clock()

def draw_radar_grid():
    screen.fill((0, 0, 0))
    green = (0, 255, 0)

    # Radar circles
    for r in range(50, RADAR_RADIUS+1, 50):
        pygame.draw.circle(screen, green, (CENTER, CENTER), r, 1)

    # Cross lines
    pygame.draw.line(screen, green, (CENTER, 0), (CENTER, SCREEN_SIZE), 1)
    pygame.draw.line(screen, green, (0, CENTER), (SCREEN_SIZE, CENTER), 1)

    # Angle labels
    font = pygame.font.SysFont("consolas", 14)
    for deg in range(0, 181, 30):
        rad = math.radians(deg)
        x = CENTER + (RADAR_RADIUS + 20) * math.cos(rad)
        y = CENTER - (RADAR_RADIUS + 20) * math.sin(rad)
        label = font.render(f"{deg}°", True, green)
        screen.blit(label, (x - 10, y - 10))

def draw_sweep(angle, dist_cm):
    # Limit distance to MAX_DISTANCE_CM
    r = min(dist_cm, MAX_DISTANCE_CM)
    r = (r / MAX_DISTANCE_CM) * RADAR_RADIUS
    rad = math.radians(angle)

    # Endpoints
    dot_x = CENTER + r * math.cos(rad)
    dot_y = CENTER - r * math.sin(rad)
    line_x = CENTER + RADAR_RADIUS * math.cos(rad)
    line_y = CENTER - RADAR_RADIUS * math.sin(rad)

    # Sweep line
    pygame.draw.line(screen, (0, 255, 0), (CENTER, CENTER), (line_x, line_y), 2)
    # Object dot
    pygame.draw.circle(screen, (255, 0, 0), (int(dot_x), int(dot_y)), 5)

# ====== Main Loop ======
running = True
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_radar_grid()
    draw_sweep(angle, distance)
    pygame.display.flip()

pygame.quit()
