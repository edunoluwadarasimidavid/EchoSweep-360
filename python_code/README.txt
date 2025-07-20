=====================================
PYTHON RADAR USING PYGAME + ARDUINO
=====================================

By Edun Oluwadarasimi David

✅ WHAT YOU NEED INSTALLED:
- Python 3.8 or later
- pip install pyserial pygame

✅ HOW TO RUN:
1. Extract this ZIP.
2. Open a terminal in the folder.
3. Run the command:
   python python_radar.py

✅ SETUP REMINDER:
- Your Arduino must be running the radar code that prints: angle,distance
- Your servo should sweep from 0 to 180 degrees
- HC-SR04 should be wired:
  TRIG → A0
  ECHO → A1
  SERVO → pin 11 (SER1)

✅ IMPORTANT:
- Edit the line in `python_radar.py`:
  SERIAL_PORT = 'COM3'
  🔁 Change 'COM3' to your actual Arduino COM port!

✅ EXIT:
- Press X on the window or use Ctrl+C in terminal.

Let me know if you want a GUI or web-based version too!
