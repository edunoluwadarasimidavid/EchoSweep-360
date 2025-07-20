# 🚀 EchoSweep 360 — Arduino Radar Scanner

**EchoSweep 360** is a microcontroller-based radar system that uses an ultrasonic sensor and a servo motor to scan the environment in a 180-degree arc. The system visualizes distances in real-time using a Python GUI interface. This project is ideal for beginners interested in robotics, embedded systems, or security scanning technologies.

> Created by **Edun Oluwadarasimi David**

---

## 🔧 Components Used

- **Arduino Uno** (or any compatible board)
- **HC-SR04 Ultrasonic Sensor**
- **SG90 or MG996R Servo Motor**
- **USB Cable** for programming
- **Jumper wires**
- **Breadboard** (optional)
- **Computer** to run the Python GUI (Windows/Linux/Mac)

---

## ⚙️ Arduino Wiring Guide

Below is the recommended wiring connection for the EchoSweep 360 system:

| Component            | Arduino Pin     | Description                              |
|---------------------|------------------|------------------------------------------|
| **Servo Motor**      | D9               | Controls the servo angle for scanning    |
| **Ultrasonic Trig**  | A0               | Triggers the sound pulse                 |
| **Ultrasonic Echo**  | A1               | Receives the reflected pulse             |
| **Servo + VCC**      | 5V               | Power supply for servo and sensor        |
| **GND (All grounds)**| GND              | Common ground for all components         |

> Ensure your power supply is stable when powering servos. Use an external 5V if needed for higher torque motors like MG996R.

---

## 🧠 How It Works

1. **Servo Movement:** The servo motor sweeps back and forth from 0° to 180°, simulating a radar scan.
2. **Distance Sensing:** At each angle step, the ultrasonic sensor sends out a sound pulse and listens for its echo.
3. **Serial Communication:** The Arduino sends the angle and distance data through serial to the computer.
4. **Real-Time GUI:** A Python or Processing interface reads this serial data and renders it as a radar-like visual.

---

## 💻 Software Requirements

To visualize the radar sweep on your computer, you can use:

### Option 1: Python (Recommended)
- **Python 3.8+**
- **Pygame** for GUI rendering  
  (`pip install pygame`)
- Serial connection (e.g., COM5 or /dev/ttyUSB0)

### Option 2: Processing IDE
- Arduino-style visual interface
- Reads serial data and draws radar visuals using graphics primitives

---

## 🧪 Use Cases

- DIY Security Scanners
- Object Mapping Projects
- Robotics Distance Detection
- Obstacle Avoidance Testbed

---

## 🏷️ Project Name Origin

The name **EchoSweep 360** was uniquely chosen to represent the combination of ultrasonic "echo" sensing and the sweeping action of the servo, forming a semi-circular (or full circular) radar-like system. No other project with this exact name was found online at the time of naming.

---

## 👤 Author

**Edun Oluwadarasimi David**  
Founder, Smart Tech Programming  
Passionate Fullstack Developer and Robotics Enthusiast

---

## 📦 Repository Contents

- `README.md` – This file
- `radar.ino` – Arduino code for scanning
- `radar_gui.py` – Python visualization app (optional)
- `processing_radar.pde` – Optional Processing interface (if included)

---

## ✅ Getting Started

1. Connect your components using the wiring guide above.
2. Upload the Arduino sketch.
3. Run the Python GUI on your computer.
4. Watch your EchoSweep 360 scan the surroundings and show real-time distances on your screen.

---

