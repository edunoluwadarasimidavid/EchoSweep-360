#include <Servo.h>

const int trigPin = A0;     // TRIG pin of ultrasonic sensor
const int echoPin = A1;     // ECHO pin of ultrasonic sensor
const int servoPin = 9;     // SER1 = D9 (confirmed working)

Servo radarServo;

int angle = 0;
int direction = 1;

void setup() {
  Serial.begin(9600);
  radarServo.attach(servoPin);       // Use the working pin
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop() {
  radarServo.write(angle);           // Move to the current angle
  delay(25);                         // Wait for servo to reach angle

  // Trigger the ultrasonic sensor
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Read echo time
  long duration = pulseIn(echoPin, HIGH, 30000); // Timeout at 30ms

  // Convert to distance in cm
  int distance = duration * 0.034 / 2;
  if (duration == 0 || distance < 0 || distance > 200) {
    distance = 200;  // Default if out of range
  }

  // Output as "angle,distance" CSV format
  Serial.print(angle);
  Serial.print(",");
  Serial.println(distance);

  // Sweep angle
  angle += direction;
  if (angle >= 180 || angle <= 0) {
    direction = -direction;  // Reverse direction
  }
}
