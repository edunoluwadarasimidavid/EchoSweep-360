import processing.serial.*;

Serial myPort;
String incomingData = "";

float angle = 0;
float distance = 0;

void setup() {
  size(600, 600);
  smooth();
  myPort = new Serial(this, Serial.list()[0], 9600);  // Adjust index if needed
  myPort.bufferUntil('\n');
}

void draw() {
  background(0);
  drawRadar();

  float r = map(distance, 0, 200, 0, 250);
  float a = radians(angle);
  float x = 300 + r * cos(a);
  float y = 300 - r * sin(a);

  // Point
  fill(0, 255, 0);
  ellipse(x, y, 8, 8);

  // Sweep line
  stroke(0, 255, 0);
  line(300, 300, x, y);
}

void drawRadar() {
  noFill();
  stroke(0, 255, 0, 80);
  ellipse(300, 300, 500, 500);
  ellipse(300, 300, 400, 400);
  ellipse(300, 300, 300, 300);
  ellipse(300, 300, 200, 200);
  ellipse(300, 300, 100, 100);

  line(300, 50, 300, 550);
  line(50, 300, 550, 300);
}

void serialEvent(Serial p) {
  incomingData = p.readStringUntil('\n');
  if (incomingData != null) {
    incomingData = trim(incomingData);
    String[] parts = split(incomingData, ',');
    if (parts.length == 2) {
      angle = float(parts[0]);
      distance = float(parts[1]);
    }
  }
}
