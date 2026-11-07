import re

text = "Call 984-765-4321 or 876 543 2109 or 123-456-7890"

pattern=re.compile(r"\d{3}.\d{3}.\d{4}")
print((pattern.search(text)).group())
print(pattern.findall(text))
