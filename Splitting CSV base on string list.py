import pandas as pd

# List of strings to search for
strings_to_search = ['LSI', 'Historical', 'The Horse']

# Read in the input CSV file as a Pandas DataFrame
df = pd.read_csv('12200.csv')

# Iterate through the strings we're searching for
for string in strings_to_search:
    # Filter the DataFrame to only include rows where the 's' column contains the current string
    df_string = df[df['x'].str.contains(string)]

    # Write the filtered DataFrame to a CSV file named after the current string
    df_string.to_csv(f'{string}.csv', index=False)


