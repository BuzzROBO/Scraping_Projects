import pandas as pd
import json

# Load the JSON data from file
with open("sample.json", "r") as file:
    json_str = file.read()
    json_data = json.loads(json_str)

# Create an empty list to store profile data
profile_data_list = []

# Iterate over each JSON object
for obj in json_data:
    # Ensure obj is a dictionary
    if isinstance(obj, dict):
        # Extract the "profile" data from each object
        profile_data = obj.get("profile", {})
        
        # Iterate over each entry in the "profile" data
        for entry_key, entry_value in profile_data.items():
            # Append each entry to the list
            profile_data_list.append(entry_value.get("data", {}))

# Create a DataFrame from the list of profile data
df_profile = pd.DataFrame(profile_data_list)

# Save the DataFrame to a CSV file
df_profile.to_csv("profile_data.csv", index=False)
