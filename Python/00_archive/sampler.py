# Packages
import serial
import time
import os
import pandas as pd

# Configuration
port = 'COM3'
csv_file = 'CSV_files/load_cell_cal.csv'
#log_time = 40
n_samples = 3000


# Open the serial port
ser = serial.Serial(port, 9600, timeout=1)
print("Connection estiablised.")

# Initialize an empty list to store the data
data = []

# Start time
start_time = time.time()
print("Starting recording...")
# Collect data
for i in range(n_samples):
    # Read a line from the serial port
    line = ser.readline()
    # Decode the line from bytes to string
    value = line.decode('utf-8').strip()
    data.append(value)
    #time.sleep( log_time / n_samples ) # Wait for set time between samples

# Close the serial port
ser.close()

time_tot = time.time() - start_time
print("Recording Complete.")
print("Time spent logging: ")
print(time_tot)
print("Storing data...")


# Check if the file exists
if os.path.isfile(csv_file): # File exists
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file)
    df_length = df.shape[1]
    column_index_str = str(df_length + 1)

else: # File does not exist
    df = pd.DataFrame()
    column_index_str = "1"

# Add new data set

df[column_index_str] = data

# Write the DataFrame back to the CSV file
df.to_csv(csv_file, index=False)

# Report
print("-------------------------------------------------------------------")
print("Data entry " + column_index_str + " logged and saved to " + csv_file + " with log time {} seconds and {} samples.".format(time_tot, n_samples))
print("-------------------------------------------------------------------")
