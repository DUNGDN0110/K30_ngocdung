import re

with open("file.xml", "r") as f:
    xml_content = f.read()

tags_and_contents = re.findall(r'<([^!][^ >]+)[^>]*>(.*?)</\1>', xml_content, re.DOTALL)

print("Cấu trúc của file XML:")
for tag, content in tags_and_contents:
    print(f"Thẻ: {tag}, Nội dung: {content}")
