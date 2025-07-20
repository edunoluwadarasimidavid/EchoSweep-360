
![EchoSweep 360 Radar Thumbnail](swep1.jpg)

# 🚀 EchoSweep 360 — Advanced Arduino Radar Scanner with Python GUI

**EchoSweep 360** is a cutting-edge radar scanning system built using an Arduino board, ultrasonic sensor, and servo motor. It visualizes real-time 180-degree environmental scanning using a feature-rich Python GUI. This project blends hardware and software seamlessly and is perfect for robotics, security, and embedded system learners.

> 🔧 Created by **Edun Oluwadarasimi David** – Fullstack Developer & Founder, Smart Tech Programming

---

## 🔩 Components Used

| Component                 | Description                                            |
|--------------------------|--------------------------------------------------------|
| **Arduino Uno**          | Microcontroller board                                  |
| **HC-SR04 Ultrasonic**   | Measures distances using sound wave pulses            |
| **SG90 / MG996R Servo**  | Controls sweeping angle                                |
| **USB Cable**            | For connecting Arduino to PC                           |
| **Breadboard & Wires**   | For easy prototyping                                   |
| **Computer (Win/Linux)** | To run the Python GUI                                  |

> *Note: Use an external 5V supply for MG996R servo to prevent power issues.*

---

## ⚙️ Arduino Wiring Diagram

| Device             | Arduino Pin | Notes                                  |
|-------------------|-------------|----------------------------------------|
| Servo Signal       | D9          | Controls radar sweep angle             |
| Ultrasonic Trig    | A0          | Sends sound pulse                      |
| Ultrasonic Echo    | A1          | Receives echo for distance calculation |
| VCC (Sensor + Servo)| 5V         | Connect to 5V (or external 5V supply)  |
| Ground             | GND         | Common ground connection               |

---

## 🧠 How the System Works

1. **Servo Rotation**: Sweeps from 0° to 180° in steps.
2. **Ultrasonic Pulse**: Triggers at each angle and listens for echo.
3. **Distance Calculation**: Based on pulse time, distance is measured.
4. **Serial Transfer**: Data is sent from Arduino to PC over USB.
5. **Python GUI**: Reads serial data, shows real-time radar animation, and plays sounds if obstacles are close.

---

## 🎨 Python GUI Features

✅ Real-time radar sweep display  
✅ Dynamic visualization of detected objects  
✅ Sound notification when obstacle is detected  
✅ Note box showing live detection messages  
✅ Animated radar visuals with sweep and dots  
✅ Exit & Minimize buttons  
✅ Fully resizable, customizable, and responsive layout  
✅ Light resource usage and cross-platform compatible  

---

## 🧰 Software Requirements

### ✅ Python GUI Requirements (Recommended)
- Python 3.8 or newer  
- [Pygame](https://www.pygame.org/) - for GUI rendering  
- [pyserial](https://pypi.org/project/pyserial/) - for serial communication

Install required libraries with:

```bash
pip install pygame pyserial
````

---

## 📁 Project Structure

```bash
EchoSweep360/
├── radar.ino             # Arduino sketch
├── python_radar.py       # Main Python GUI script
├── swep1.jpg             # Project thumbnail (used in README)
├── README.md             # You’re reading it!
└── assets/               # Optional folder for future icons/sounds
```

---

## ✅ Setup Instructions

### 🔌 Hardware Setup

1. Wire the Arduino, sensor, and servo using the provided pin guide.
2. Ensure stable power for servo (especially MG996R).

### 💡 Arduino Upload

1. Open `radar.ino` in the Arduino IDE.
2. Select your board and COM port.
3. Upload the code to your Arduino.

### 🖥️ Python GUI Launch

1. Plug the Arduino into your PC (COM port like `COM3`, `COM5`, etc.).
2. Open `python_radar.py` in any Python IDE or terminal.
3. Edit the serial port in the code (`COM5` by default) to match yours.
4. Run the GUI.

```bash
python python_radar.py
```

---

## 🔊 Advanced Features in the GUI

* 🔔 **Sound Notification**: Buzzer sound when object is within critical range.
* 📝 **Note Box**: Displays detection messages like `⚠️ Object at 32cm`.
* 🛑 **Exit Button**: Cleanly shuts down the interface.
* 🔽 **Minimize Button**: Minimizes the GUI to the taskbar.
* 🔄 **Smooth Animation**: Radar sweep rotates fluidly with radar beam effect.
* 💻 **Resizable Window**: Adjust GUI size as needed.
* 🚀 **Performance Friendly**: Low CPU/GPU usage with smooth drawing.

---

## 📌 Real Use Cases

* Home-made security scanners
* Obstacle detection in robotics
* Real-time mapping for autonomous bots
* AI vision pre-mapping tool
* Embedded systems and robotics education

---

## 📛 Why "EchoSweep 360"?

**Echo**: From ultrasonic echo waves
**Sweep**: From the servo scanning motion
**360**: Symbolizing full coverage & awareness (though sweep is 180°)

> The name was crafted uniquely for this project. No other known radar system uses the same branding.

---

## 👨‍💻 Author

**Edun Oluwadarasimi David**
📧 [davidedun2010@gmail.com](mailto:davidedun2010@gmail.com)
🌐 [Smart Tech Programming](https://edunoluwadarasimidavid.name.ng/)
💼 Fullstack Developer | Robotics Enthusiast | Community Builder

---

## 💬 Support & Contribution

Got an improvement idea or want to help?
Pull requests and feature suggestions are welcome!
Let’s make EchoSweep 360 even better together.

---

## ✅ To Do / Future Features

* 📡 Auto-rotation support (with dual servo)
* 🌐 Web-based live scan dashboard (React/Python)
* 🔁 Full 360° scanning support
* 📈 Logging distances to CSV or live graph
* 🎮 Game controller support for manual sweep

---

## 📢 Final Note

This project is meant to inspire and educate. It’s a powerful demonstration of how **hardware + software + creativity** can come together to build meaningful systems.

**Happy Building! 🛠️**

-
