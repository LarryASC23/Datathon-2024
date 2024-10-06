import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv(r"C:\Users\ldls0\Downloads\data\USDA_PDP_AnalyticalResults.csv")

# Define the states and their abbreviations
states = {
    'Texas': 'TX',
    'Oklahoma': 'OK',
    'Missouri': 'MO',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Ohio': 'OH',
    'Louisiana': 'LA',
    'Mississippi': 'MS',
    'Alabama': 'AL',
    'Georgia': 'GA',
    'Florida': 'FL',
    'South Carolina': 'SC',
    'North Carolina': 'NC',
    'Virginia': 'VA',
    'Maryland': 'MD',
    'Pennsylvania': 'PA',
    'New York': 'NY',
    'Vermont': 'VT',
    'California': 'CA',
    'Oregon': 'OR',
    'Washington': 'WA',
    'Nebraska': 'NE',
    'Kansas': 'KS',
    'Minnesota': 'MN'
}

# Create a dictionary to store results for each state
state_pesticide_counts = {state: pd.Series(dtype=int) for state in states}

# Loop through the years 1993 to 2023 for each state
for year in range(1993, 2024):
    for state, abbr in states.items():
        # Construct the Sample ID prefix for each state
        if year < 2000:
            year_suffix = str(year - 1900).zfill(2)  # 1990s range (TX93, OK93, ...)
        else:
            year_suffix = str(year - 2000).zfill(2)  # 2000s range (TX00, OK00, ...)
        
        sample_id_prefix = f'{abbr}{year_suffix}'
        
        # Filter the DataFrame for 'Sample ID' starting with the constructed prefix
        filtered_df = df[df['Sample ID'].str.startswith(sample_id_prefix)]
        
        # Count occurrences of each 'Pesticide Name'
        pesticide_counts = filtered_df['Pesticide Name'].value_counts()
        
        # Add yearly counts to the state pesticide counts
        state_pesticide_counts[state] = state_pesticide_counts[state].add(pesticide_counts, fill_value=0)

# Get the top 5 most common pesticides for each state
for state, total_counts in state_pesticide_counts.items():
    top_5_pesticides = total_counts.nlargest(5)  # Get top 5 for each state
    print(f"\nThe top 5 most common pesticides in {state} from 1993 to 2023 are:")
    for pesticide, count in top_5_pesticides.items():
        print(f"'{pesticide}' with {count} occurrences.")
