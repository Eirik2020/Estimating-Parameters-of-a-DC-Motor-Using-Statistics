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
    // Read and print AS5600 data
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
        Serial.print(","); 
    }
    
    // Read and print INA219 data
    float shuntVoltage_mV = ina219.getShuntVoltage_mV(); 
    float busVoltage_V = ina219.getBusVoltage_V();
    float current_mA = ina219.getCurrent_mA();
    Serial.print(busVoltage_V);
    Serial.print(",");
    Serial.print(shuntVoltage_mV); 
    Serial.print(",");
    Serial.println(current_mA);
}
