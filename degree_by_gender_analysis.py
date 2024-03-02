import pandas as pd
import matplotlib.pyplot as plt

# Read data from Excel file
df = pd.read_excel("assets/Degree_By_Gender_200813.xlsx")

# Set index to 'Field of Study'
df.set_index('Field of Study', inplace=True)

# Plot the bar graph
ax = df[['Attained bachelor\'s degree (Total)', 'Attained associate\'s degree (Total)',
         'Attained certificate (Total)', 'No degree, still enrolled (Total)',
         'No degree, not enrolled (Total)']].plot(kind='bar', figsize=(12, 8), colormap='Paired')

# Add title and labels
plt.title("Percentage of Attainment or Level at Last Institution Enrolled by Field of Study")
plt.xlabel("Field of Study")
plt.ylabel("Percentage")
plt.xticks(rotation=45, ha='right')

# Show the plot
plt.legend(title='Total', loc='upper right')
plt.tight_layout()
plt.show()