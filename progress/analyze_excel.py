import pandas as pd

# Read the Excel sheet into a DataFrame
df = pd.read_csv(r"C:\Users\ldls0\Downloads\data\USDA_PDP_AnalyticalResults.csv")

# Display the first few rows (optional, for verification)
# print(df.head())

# Filter the DataFrame for 'Sample ID' starting with 'TX'
filtered_df = df[df['Sample ID'].str.startswith('TX00')]

# Count occurrences of each 'Pesticide Name'
pesticide_counts = filtered_df['Pesticide Name'].value_counts()

# Display the most common pesticide
most_common_pesticide = pesticide_counts.idxmax()
most_common_count = pesticide_counts.max()

# print(f"The most common pesticide is '{most_common_pesticide}' with {most_common_count} occurrences.")

df.info()