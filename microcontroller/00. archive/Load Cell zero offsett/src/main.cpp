// PlatformIO project setup for Arduino Mega
// Ensure your platformio.ini is set up correctly for Arduino Mega

#include <Arduino.h>
#include <Wire.h>
#include "AS5600.h"

AS5600 as5600;

void setup() {
 Serial.begin(115200); // Start serial communication at 115200 baud
 Wire.begin(); // Initialize I2C communication

 if (!as5600.begin()) { // Check if the sensor is successfully initialized
    Serial.println("Failed to connect to AS5600 sensor."); // Print error message if connection fails
 } else {
    Serial.println("Connected to AS5600 sensor."); // Print success message if connection is successful
 }
}

void loop() {
 uint16_t rawAngle = as5600.readAngle(); // Read the raw angle
 float angleDegrees = rawAngle * AS5600_RAW_TO_DEGREES; // Convert to degrees
 Serial.println(angleDegrees); // Send the angle over serial
 delay(1000); // Wait for 1 second
}
