import pandas as pd
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt



# Step 1: Read the CSV file into a DataFrame
df = pd.read_csv('CSV_files/load_cell_cal.csv')


# Step 2: Calculate the mean of each column
means = df.mean()

# Step 3: Store the means in a list
means_list = means.tolist()


weights = []
for i in range(len(means_list)):
    weights.append(36.8 + 20.2565*i )


# Data
x = np.array(means_list)
y = np.array(weights)

# Perform linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

# Generate y values for the regression line
y_pred = slope * x + intercept

print("Alpha:")
print(slope)
print("beta")
print(intercept)
# Plot the data and the regression line
plt.scatter(x, y, color='blue', label='Original Data')
plt.plot(x, y_pred, color='red', label='Regression Line')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
