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

# Initialize an empty list to store the results
results_list = []

# Loop through each state and gather data for the specific pesticides
for state, abbr in states.items():
    # Initialize a dictionary to store the counts for the state
    pesticide_counts = {pesticide: 0 for pesticide in pesticides_of_interest}
    
    for year in range(1993, 2023):
        # Construct the Sample ID prefix for each state
        if year < 2000:
            year_suffix = str(year - 1900).zfill(2)  # 1990s range
        else:
            year_suffix = str(year - 2000).zfill(2)  # 2000s range
        
        sample_id_prefix = f'{abbr}{year_suffix}'
        
        # Filter the DataFrame for 'Sample ID' starting with the constructed prefix
        filtered_df = df[df['Sample ID'].str.startswith(sample_id_prefix)]
        
        # Further filter to only include rows where 'Pesticide Name' matches any in the pesticides_of_interest
        filtered_pesticides_df = filtered_df[filtered_df['Pesticide Name'].isin(pesticides_of_interest)]
        
        # Count occurrences of each pesticide in the filtered data
        counts = filtered_pesticides_df['Pesticide Name'].value_counts()
        
        # Update the pesticide_counts dictionary
        for pesticide in pesticides_of_interest:
            pesticide_counts[pesticide] += counts.get(pesticide, 0)
    
    # Append the results to the list
    for pesticide, count in pesticide_counts.items():
        results_list.append({'State': state, 'Pesticide': pesticide, 'Count': count})

# Convert the list of results to a DataFrame
abundance_results = pd.DataFrame(results_list)

# Save the results to a CSV file
abundance_results.to_csv('pesticide_abundance_by_state.csv', index=False)
print("Saved pesticide abundance results to 'pesticide_abundance_by_state.csv'.")
