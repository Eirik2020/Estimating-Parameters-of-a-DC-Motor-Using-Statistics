""" Example """
# Packages
import seaborn as sns
import matplotlib.pyplot as plt
import os


# Load example dataset
tips = sns.load_dataset("tips")

# Create a Seaborn plot
sns.scatterplot(x="total_bill", y="tip", data=tips)

# Display the plot
plt.show()


# Save plot
folder_name = "figures" # Folder name
file_name = "heyhey_plot.pdf" # Plot name
file_path = os.path.join(folder_name, file_name) # Generate file path
plt.savefig(file_path, format='pdf')



# OVERLEAF CODE
# Packages
"""
\documentclass{article}
\usepackage{graphicx}
"""

# Figure formatting ( !Replace "seaborn_plot.pdf" with your plot!, also figures in applicable. 
"""

\begin{figure}[htbp]
    \centering
    \includegraphics[width=\linewidth]{figures/seaborn_plot.pdf}
    \caption{Seaborn scatter plot}
    \label{fig:seaborn}
\end{figure}

Figure \ref{fig:seaborn} shows the scatter plot created using Seaborn, rescaled to fit the page width and centered within the document.

"""