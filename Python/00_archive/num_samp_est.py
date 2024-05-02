# Packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Define +- error percent tolerance
err = 0.001

## Data processing ##
# Step 1: Read the CSV file into a DataFrame
df = pd.read_csv('CSV_files/sample_time_test.csv')

# Convert to np array
numpy_array = df.to_numpy()

# Calculate mean values for all sample sizes.
array_size = numpy_array.size
mean_values = np.array([])
for i in range(array_size):
    mean = np.mean(numpy_array[:(i+1)])
    mean_values = np.append(mean_values, mean)

# Calculate mean error vs number of samples.
last_element = mean_values[-1]
error_list = np.array([])
for k in range(len(mean_values)):
    error = abs(last_element - mean_values[k])
    error_list = np.append(error_list, error)

# Float to search, and tolerance.
val, tol = err, err * last_element

# Find the index of the first element close to val within the tolerance
index = next(i for i, _ in enumerate(error_list) if np.isclose(_, val, tol))
print('Index for the first sample within +-{} percent of {} samples is: {}'.format(err, array_size, index))
num_samp_string = str(index) + " samples with +-" + str(err) +"% error."

# Plotting
# Generate x values
start = 1
end = array_size
num_values = array_size
x_values = np.linspace(start, end, num_values)

# Apply Seaborn style
sns.set()

# Plot as a line plot
plt.plot(x_values, error_list, label='Error vs sample size') # Error vs sample size
plt.axvline(index, color='r', linestyle='--', label=num_samp_string)

# Set plot limits and axis names.
plt.xlabel('Samples')
plt.ylabel('RMS Error')
plt.title("RMS Error vs number of samples.")
plt.xlim(x_values[0], x_values.size)

# Get the current Axes instance
ax = plt.gca()

# Increase the number of ticks on the x and y axes
ax.set_xticks(np.linspace(0, x_values.size, 10)) # Adjust the number of ticks on the x-axis
ax.set_yticks(np.linspace(np.min(error_list), np.max(error_list), 10)) # Adjust the number of ticks on the y-axis

print(error_list[index])
plt.legend()
plt.show()
