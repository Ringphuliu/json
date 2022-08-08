import json
a={}
filename="meraki_7.txt"
with open(filename) as f:
    for i in f:
        key,value=i.strip().split(None,1)
        a[key]=value
print(json.dumps(a,indent=4))
file=open("meraki7.json","w")
json.dump(a,file,indent=4)
file.close()                                                                                                                                                                                                                                                                                                                                                     