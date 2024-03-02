import pandas as pd
import matplotlib.pyplot as plt

# Read data from Excel file
df_total = pd.read_excel("assets/Degree_By_Gender_200812.xlsx", sheet_name="Total")
df_male = pd.read_excel("assets/Degree_By_Gender_200812.xlsx", sheet_name="Male")
df_female = pd.read_excel("assets/Degree_By_Gender_200812.xlsx", sheet_name="Female")
print(df_total)
print(df_male)
print(df_female)
# Set index to 'Field of Study'
df_total.set_index('Field of Study', inplace=True)
columns = columns = [
    "Attained bachelor's degree",
    "Attained associate's degree",
    "Attained certificate",
    "No degree, still enrolled",
    "No degree, not enrolled"
]
# Plot the bar graph
ax = df_total[columns].plot(kind='bar', figsize=(12, 8), colormap='Paired')
ax = df_male[columns].plot(kind='bar', figsize=(12, 8), colormap='Paired')
ax = df_female[columns].plot(kind='bar', figsize=(12, 8), colormap='Paired')

# Add title and labels
plt.title("Percentage of Attainment or Level at Last Institution Enrolled by Field of Study")
plt.xlabel("Field of Study")
plt.ylabel("Percentage")
plt.xticks(rotation=45, ha='right')

# Show the plot
plt.legend(title='Total', loc='upper right')
plt.tight_layout()
plt.show()