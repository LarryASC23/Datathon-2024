import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv(r"C:\Users\ldls0\Downloads\data\USDA_PDP_AnalyticalResults.csv")

# Create a dictionary to store results for each year
yearly_pesticide_counts = {}

# Create a Series to accumulate pesticide counts across all years
total_pesticide_counts = pd.Series(dtype=int)

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
    
    # Add yearly counts to the total pesticide counts
    total_pesticide_counts = total_pesticide_counts.add(pesticide_counts, fill_value=0)
    
    # Find the most common pesticide for the year
    if not pesticide_counts.empty:
        most_common_pesticide = pesticide_counts.idxmax()
        most_common_count = pesticide_counts.max()
        # Store the result for the year
        yearly_pesticide_counts[year] = (most_common_pesticide, most_common_count)
    else:
        # Handle the case where there are no results for the year
        yearly_pesticide_counts[year] = ("No data", 0)

# Get the top 5 most common pesticides across all years
top_5_pesticides = total_pesticide_counts.nlargest(5)

# Display the results for each year
for year, (pesticide, count) in yearly_pesticide_counts.items():
    print(f"The most common pesticide in Texas in {year} is '{pesticide}' with {count} occurrences.")

# Display the top 5 most common pesticides across all years
print("\nThe top 5 most common pesticides in Texas from 1993 to 2023 are:")
for pesticide, count in top_5_pesticides.items():
    print(f"'{pesticide}' with {count} occurrences.")
