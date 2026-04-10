# Get a JSON file from the City of Chicago's Data Portal and analyze driver types

import pandas as pd
import requests

# Create a REST query to get the JSON data for driver types

search_results = requests.get("https://data.cityofchicago.org/resource/97wa-y6ff.json?$select=driver_type,count(license)&$group=driver_type")

results_json = search_results.json()
print("Driver Types and their Counts:")
print(results_json)

# Convert the JSON results to a DataFrame for easier analysis
results_df = pd.DataFrame(results_json)
results_df.columns = ["driver_type", "count"]
results_df = results_df.set_index("driver_type")

print("\nDriver Types and their Counts (DataFrame):")
print(results_df)