import re

with open("file.json", "r") as f:
    json_content = f.read()

key_value_pairs = re.findall(r'"([^"]+)":\s*(".*?"|\d+\.\d+|\d+)', json_content)

print("Cấu trúc của file JSON:")
for key, value in key_value_pairs:
    print(f"Key: {key}, Value: {value}")
