import pandas as pd
import matplotlib
import sqlite3
import os
#from data_analysis import responses

#matplotlib.use('Agg')  # Set the backend to Agg
import matplotlib.pyplot as plt

# Read data from survey file

print("this is happending")
def graph_survey():
  
  #Make survey to pull from database

  df = pd.read_excel("assets/mock_data.xlsx")
  
  imposter_count = {"yes": 0, "no": 0}

  for imposter_check in df["imposter"]:
    if imposter_check == "yes":
      imposter_count["yes"] += 1
    else:
      imposter_count["no"] += 1

  df.set_index('imposter', inplace=True)
  df_imposter = pd.DataFrame(data=imposter_count, index=[0])

  # Plot the bar graph
  ax = df_imposter.plot.bar(rot=0, color=['#a4dcf4', '#d28997'])
  #ax = df[columns].plot(kind='bar', figsize=(12, 8), colormap='Paired')

  # Add title and labels
  plt.title("Imposter Syndrome Count")
  plt.xlabel("Imposter Syndrome (Y/N)", fontweight='bold')
  plt.ylabel("Count", fontweight='bold')
  
  plt.xticks(rotation=45, ha='right')

  # Show the plot
  plt.legend(title='Total', loc='upper left', bbox_to_anchor=(1.05, 1))
  plot_file_path = os.path.join('static/imposter_plot.png')
  plt.tight_layout()
  plt.savefig(plot_file_path)
  return plot_file_path


if __name__ == "__main__":
  graph_survey()

