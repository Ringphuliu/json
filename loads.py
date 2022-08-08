# load
# import json
# with open("dump.json","r")as f:
#     x=json.load(f)
# print(x)

# loads
import json
string='{"1":"one","2":"two"}'
x=json.loads(string)
print(type(x))