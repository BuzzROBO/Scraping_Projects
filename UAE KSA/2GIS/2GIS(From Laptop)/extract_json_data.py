import os
import json
import csv

# Function to extract data from a JSON file
def extract_data_from_json(json_file):
    with open(json_file, 'r') as file:
        profile_data = json.load(file)
    extracted_data = []
    for key in profile_data["profile"]:
        data_content = profile_data["profile"][key].get("data")
        if data_content:
            extracted_data.append({
                "makani": data_content.get("address", {}).get("makani"),
                #"name": data_content.get("address", {}).get("name"),
                "address_comment": data_content.get("address_comment"),
                "address_name": data_content.get("address_name"),
                "legal_name": data_content.get("name_ex", {}).get("legal_name"),
                "primary": data_content.get("name_ex", {}).get("primary"),
                "city_alias": data_content.get("city_alias"),
                "full_name": data_content.get("full_name"),
                "lat": data_content.get("point", {}).get("lat"),
                "lon": data_content.get("point", {}).get("lon"),
                "purpose_name": data_content.get("purpose_name"),
                "general_rating": data_content.get("reviews",{}).get("general_rating"),
                "general_review_count": data_content.get("reviews",{}).get("general_review_count")
            })
    return extracted_data

# Path to the folder containing JSON files
folder_path = "./json_data1"

# List to store extracted data
all_data = []

# Iterate over each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".json"):
        json_file_path = os.path.join(folder_path, filename)
        extracted_data = extract_data_from_json(json_file_path)
        all_data.extend(extracted_data)

# Path to save CSV file
csv_file_path = "./2gis.csv"

# Writing data to CSV file
with open(csv_file_path, mode='w', newline='') as file:
    fieldnames = [
        "makani",
        #"name",
        "building_name",
        "address_comment",
        "address_name",
        "legal_name",
        "primary",
        "city_alias",
        "full_name",
        "lat",
        "lon",
        "purpose_name",
        "general_rating",
        "general_review_count"
    ]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader()
    for data in all_data:
        writer.writerow(data)

print("CSV file has been created successfully!")

# Printing the extracted data
print("\nExtracted Data:")
for index, data in enumerate(all_data, start=1):
    print(f"\nEntry {index}:")
    for key, value in data.items():
        print(f"{key}: {value}")
