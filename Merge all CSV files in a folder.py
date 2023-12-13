import os
import glob
import pandas as pd

path = r'C:\Users\e095645\PycharmProjects\pythonProject\x' # Change to the path of your csv files
all_files = glob.glob(os.path.join(path, "*.csv")) # Select all csv files

df_merged = pd.DataFrame() # Initialize an empty dataframe

for file in all_files:
    df = pd.read_csv(file, index_col=None, header=0) # Read each file
    df_merged = pd.concat([df_merged, df], axis=0, ignore_index=True) # Concatenate the dataframes

df_merged.to_csv('merged_csv.csv', index=False) # Write the final dataframe to a csv file


