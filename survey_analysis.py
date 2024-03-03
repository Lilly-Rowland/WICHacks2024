import pandas as pd
import matplotlib
import sqlite3
import os
#from data_analysis import responses

matplotlib.use('Agg')  # Set the backend to Agg
import matplotlib.pyplot as plt

# Read data from survey file

def add_data()

def graph_survey():
  
  conn = sqlite3.connect('new_database.db')

  # Execute SQL query and read data into a DataFrame
  query = "SELECT * FROM Response;"
  df = pd.read_sql_query(query, conn)

  # Close the database connection
  conn.close()

  # Now you have your data in the DataFrame 'df'
  print(df.head())  # Display the first few rows of the DataFrame

  print(len(responses))
  

if __name__ == "__main__":
  graph_survey()
