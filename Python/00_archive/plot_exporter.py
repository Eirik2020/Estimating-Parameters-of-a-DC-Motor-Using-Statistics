""" Example """
# Packages
import seaborn as sns
import matplotlib.pyplot as plt
import os


# Load example dataset
tips = sns.load_dataset("tips")

# Create a Seaborn plot
sns.scatterplot(x="total_bill", y="tip", data=tips)

# Enable saving plots
SAVE = True

# Save plot
folder_name = "Python/figures" # Folder name
file_name = "heyhey_plot.pdf" # Plot name
file_path = os.path.join(folder_name, file_name) # Generate file path
if SAVE:
    plt.savefig(file_path, format='pdf')

# Display the plot
plt.show()

