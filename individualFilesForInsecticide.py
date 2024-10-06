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

# List of pesticides of interest
pesticides_of_interest = ['Atrazine', 'Thiabendazole', 'Pyraclostrobin', 'Imidacloprid', 'Desethyl atrazine']

# Loop through each pesticide and save individual files for each one
for pesticide in pesticides_of_interest:
    # Initialize an empty list to store the results for the current pesticide
    results_list = []

    # Loop through each state and gather data for the current pesticide
    for state, abbr in states.items():
        # Initialize a count for the state
        pesticide_count = 0
        
        for year in range(1993, 2023):
            # Construct the Sample ID prefix for each state
            if year < 2000:
                year_suffix = str(year - 1900).zfill(2)  # 1990s range
            else:
                year_suffix = str(year - 2000).zfill(2)  # 2000s range
            
            sample_id_prefix = f'{abbr}{year_suffix}'
            
            # Filter the DataFrame for 'Sample ID' starting with the constructed prefix
            filtered_df = df[df['Sample ID'].str.startswith(sample_id_prefix)]
            
            # Further filter to only include rows where 'Pesticide Name' matches the current pesticide
            filtered_pesticide_df = filtered_df[filtered_df['Pesticide Name'] == pesticide]
            
            # Count occurrences of the pesticide in the filtered data
            pesticide_count += len(filtered_pesticide_df)
        
        # Append the results to the list
        results_list.append({'State': state, 'Pesticide': pesticide, 'Count': pesticide_count})

    # Convert the list of results to a DataFrame
    pesticide_results = pd.DataFrame(results_list)

    # Save the results to a CSV file for the current pesticide
    file_name = f'{pesticide}_abundance_by_state.csv'.replace(' ', '_')
    pesticide_results.to_csv(file_name, index=False)
    print(f"Saved results for {pesticide} to '{file_name}'.")
