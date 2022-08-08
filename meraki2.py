import json
a= {
  "name": "David",
  "class":"I",
  "age": 6  
}
# print(type(a))
b = json.dumps(a)
print(b)