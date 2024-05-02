import serial
import time

# Replace 'COM3' with the port your Arduino is connected to
arduino_port = 'COM3'

# Open the serial port
ser = serial.Serial(arduino_port, 9600, timeout=1)

# Rename the variable to avoid conflict with the time module
time_duration = 10
t = 0
try:
    while True:
        # Read a line from the serial port
        line = ser.readline()
        # Decode the line from bytes to string
        line = line.decode('utf-8').strip()
        # Print the value
        print(f'Analog Value: {line}')
        # Wait for a bit before reading the next value
        t += 0.1
        time.sleep(0.1) # Use the time module correctly here
except KeyboardInterrupt:
    # Close the serial port when the script is interrupted
    ser.close()
    print("Serial port closed.")

ser.close()
print("Serial port closed.")
