import serial
import time
import os
import pandas as pd

# Configuration
port = 'COM3'
csv_file = 'test.csv'
n_samples = 100

# Open the serial port
ser = serial.Serial(port, 9600, timeout=1)
print("Connection established.")

# Initialize empty lists to store the data
bus_voltage = []
shunt_voltage = []
current = []
angle = []
t = []

# Start time
start_time = time.time()
print("Starting recording...")

# Collect data
for i in range(n_samples):
    line = ser.readline().decode('utf-8').strip()
    if line:
        # Parse and store data
        data = line.split(',')
        if len(data) == 4:
            angle_raw = float(data[0])
            bus_voltage.append(float(data[1]))  # Convert to float
            shunt_voltage.append(float(data[2]))  # Convert to float
            current.append(float(data[3]))  # Convert to float
            angle.append(angle_raw)
            t.append(time.time() - start_time)

# Close the serial port
ser.close()

time_tot = time.time() - start_time
print("Recording Complete.")
print("Time spent logging: {:.2f} seconds".format(time_tot))
print("Storing data...")

# Create a DataFrame from the collected data
df = pd.DataFrame({
    'Angle': angle,
    'V_bus': bus_voltage,
    'V_shunt': shunt_voltage,
    'current': current,
    'time': t
})

# Check if the file exists, and append or create accordingly
if os.path.isfile(csv_file):  # File exists
    # Read the CSV file into a DataFrame
    df_old = pd.read_csv(csv_file)

    # Concatenate the old DataFrame with the new one
    df = pd.concat([df_old, df], axis=1)

# Write the DataFrame to the CSV file
df.to_csv(csv_file, index=False)

# Report
print("-------------------------------------------------------------------")
print("Data saved to {}: {} samples recorded in {:.2f} seconds".format(csv_file, n_samples, time_tot))
print("-------------------------------------------------------------------")

