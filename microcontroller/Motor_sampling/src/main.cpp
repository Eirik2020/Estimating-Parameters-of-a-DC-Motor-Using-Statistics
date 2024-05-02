#include <Arduino.h>
#include <Wire.h>
#include <Adafruit_INA219.h>

#define AS5600_ADDRESS 0x36

Adafruit_INA219 ina219;

void setup() {
    Wire.begin();
    Serial.begin(9600);

    if (!ina219.begin()) {
        Serial.println("Failed to find INA219 chip");
        while (1);
    }

    ina219.setCalibration_32V_2A();
}

void loop() {
    Wire.beginTransmission(AS5600_ADDRESS);
    Wire.write(0x0E);
    Wire.endTransmission();
    Wire.requestFrom(AS5600_ADDRESS, 2);

    if (Wire.available() >= 2){
        int highByte = Wire.read();
        int lowByte = Wire.read();
        int angle_raw = (highByte << 8) | lowByte;

        float angle_degrees = (angle_raw * 360.0) / 4096.0;
        Serial.print(angle_degrees);
        Serial.println();  // Added this line to print a newline character after each angle
    }
}
