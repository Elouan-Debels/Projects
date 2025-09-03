import json

# Read the original JSON file
with open('D:/assignment 2 data/code/dataset.json', 'r') as file:
    data = json.load(file)

# Create a new list to store filtered data
filtered_data = []

# Iterate over each entry in the original data
for entry in data:
    filtered_entry = {
        "appid": entry["appid"],
        "sentiment": entry.get("sentiment"),  # Using get() to handle the case where sentiment may be missing
        "screenshots": entry["screenshots"]
    }
    filtered_data.append(filtered_entry)

# Write the filtered data to a new JSON file
with open('D:/assignment 2 data/code/sentiment.json', 'w') as outfile:
    json.dump(filtered_data, outfile, indent=4)

