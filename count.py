import json
# 文件路径
file_path = '/Users/a123/Desktop/2023 全球地铁迭代/231220 全球地铁/Metro/public/data.json'

# 初始化计数器
city_count = 0
line_count = 0

# 读取并解析 JSON 文件
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)
    
    # 遍历每个城市
    for city in data:
        # 增加城市计数
        city_count += 1
        
        # 增加该城市的地铁线路计数
        line_count += len(city["地铁线路"])

# 输出结果
print(f'总共有 {city_count} 个城市')
print(f'总共有 {line_count} 条地铁线路')


# 计算每个城市有多少条线路
# import json
# import csv

# # Function to read a JSON file
# def read_json(file_path):
#     with open(file_path, 'r', encoding='utf-8') as file:
#         return json.load(file)

# # Specify the JSON file path
# file_path = '/Users/a123/Desktop/2023 全球地铁迭代/231220 全球地铁/Metro/public/data.json'  # Use your actual file path

# # Read the JSON file
# data = read_json(file_path)

# # Collect all line names
# line_names = []
# for city in data:
#     for line in city["地铁线路"]:
#         line_names.append(line['线路'])

# # Write the line names to a CSV file
# csv_file_path = '/Users/a123/Desktop/2023 全球地铁迭代/231220 全球地铁/Metro/public/lines.csv'
# with open(csv_file_path, 'w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerow(['线路名称'])  # Writing the header
#     for name in line_names:
#         writer.writerow([name])

# print(f"线路名称已保存到 {csv_file_path}")
