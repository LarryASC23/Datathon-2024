import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv(r"C:\Users\ldls0\Downloads\data\USDA_PDP_AnalyticalResults.csv")

# Create a dictionary to store results for each year
yearly_pesticide_counts = {}

# Loop through the years 1993 to 2023
for year in range(1993, 2024):
    # Construct the Sample ID prefix:
    # For years in the 1990s, use TX followed by the last two digits of the year (TX93 for 1993, etc.)
    # For years in the 2000s, also use TX followed by the last two digits of the year (TX00 for 2000, etc.)
    
    if year < 2000:
        year_suffix = str(year - 1900).zfill(2)  # 1990s range (TX90, TX91, ...)
    else:
        year_suffix = str(year - 2000).zfill(2)  # 2000s range (TX00, TX01, ...)
    
    sample_id_prefix = f'TX{year_suffix}'
    
    # Filter the DataFrame for 'Sample ID' starting with the constructed prefix
    filtered_df = df[df['Sample ID'].str.startswith(sample_id_prefix)]
    
    # Count occurrences of each 'Pesticide Name'
    pesticide_counts = filtered_df['Pesticide Name'].value_counts()
    
    # Find the most common pesticide for the year
    if not pesticide_counts.empty:
        most_common_pesticide = pesticide_counts.idxmax()
        most_common_count = pesticide_counts.max()
        # Store the result for the year
        yearly_pesticide_counts[year] = (most_common_pesticide, most_common_count)
    else:
        # Handle the case where there are no results for the year
        yearly_pesticide_counts[year] = ("No data", 0)

# Display the results for each year
for year, (pesticide, count) in yearly_pesticide_counts.items():
    print(f"The most common pesticide in {year} is '{pesticide}' with {count} occurrences.")
