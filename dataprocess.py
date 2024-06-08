import json

# Function to read a JSON file
def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# Function to write to a JSON file
def write_json(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# The path to the original JSON file
input_file_path = '/Users/a123/Desktop/2023 全球地铁迭代/231220 全球地铁/Metro/public/data_origin.json'

# The path for the updated JSON file
output_file_path = '/Users/a123/Desktop/2023 全球地铁迭代/231220 全球地铁/Metro/public/data.json'

# Read the original JSON file
data = read_json(input_file_path)

# Add "城市英文标准" field for each city
for city in data:
    parts = city["城市英文"].split()
    city["城市英文标准"] = ", ".join(parts[::-1])

# Write the modified data to a new JSON file
write_json(data, output_file_path)
