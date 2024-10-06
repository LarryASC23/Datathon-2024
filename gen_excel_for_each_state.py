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

# Loop through the years 1993 to 2023 for each state
for state, abbr in states.items():
    state_data = pd.DataFrame()  # Initialize an empty DataFrame to accumulate data for the state
    
    for year in range(1994, 2024):
        # Construct the Sample ID prefix for each state
        if year < 2000:
            year_suffix = str(year - 1900).zfill(2)  # 1990s range (TX93, OK93, ...)
        else:
            year_suffix = str(year - 2000).zfill(2)  # 2000s range (TX00, OK00, ...)
        
        sample_id_prefix = f'{abbr}{year_suffix}'
        
        # Filter the DataFrame for 'Sample ID' starting with the constructed prefix
        filtered_df = df[df['Sample ID'].str.startswith(sample_id_prefix)]
        
        # Append the filtered data to the state's DataFrame
        state_data = pd.concat([state_data, filtered_df])
    
    # Save the state's data to a CSV file
    if not state_data.empty:
        state_data.to_csv(f"{state}_pesticide_data.csv", index=False)
        print(f"Saved data for {state} to {state}_pesticide_data.csv.")
    else:
        print(f"No data available for {state}.")
