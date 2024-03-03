import pandas as pd
import matplotlib
import os

matplotlib.use('Agg')  # Set the backend to Agg
import matplotlib.pyplot as plt

# Read data from Excel file

def graph_deg_by_gender():
    df_male = pd.read_excel("assets/Degree_By_Gender.xlsx", sheet_name="Male")
    df_female = pd.read_excel("assets/Degree_By_Gender.xlsx", sheet_name="Female")

    bs_deg = "Attained bachelor's degree"
    data = {'Field of Study': df_female["Field of Study"], 
            #'Total': df_total[bs_deg].tolist(),
            'Male': df_male[bs_deg].tolist(),
            'Female': df_female[bs_deg].tolist()}  
    df = pd.DataFrame.from_dict(data)  

    for item in data.get('Field of Study'):
        item.strip("\n")
        item.strip()
    # Print the output.  
    #print(df)  
    # Set index to 'Field of Study'
    df.set_index('Field of Study', inplace=True)
    columns = df.index.values.tolist()

    # Plot the bar graph
    ax = df.plot.bar(rot=0, stacked="true", color=['#a4dcf4', '#d28997'])
    #ax = df[columns].plot(kind='bar', figsize=(12, 8), colormap='Paired')

    # Add title and labels
    plt.title("Percentage of Women in STEM Subjects")
    plt.xlabel("Field of Study", fontweight='bold')
    plt.ylabel("Percentage", fontweight='bold')
    
    plt.xticks(rotation=45, ha='right')

    # Show the plot
    plt.legend(title='Total', loc='upper left', bbox_to_anchor=(1.05, 1))
    plot_file_path = os.path.join('static/plot.png')
    plt.tight_layout()
    plt.savefig(plot_file_path)
    return plot_file_path

if __name__ == '__main__':
    plot_file = graph_deg_by_gender()