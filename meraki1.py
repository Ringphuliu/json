import json
a=  '{ "Name":"David", "Class":"I", "Age":6 }'
b= json.loads(a)
# print("JSON data:")
# print(b)
print("Name:" ,b["Name"])
print("Class: ",b["Class"])
print("Age:",b["Age"])