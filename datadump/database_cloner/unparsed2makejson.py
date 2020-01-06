import requests
import json
import sys
from seapie import Seapie as seapie

partnum = sys.argv[1]

with open("part_" + partnum + ".csv", "r") as file:
    names = file.read()
names = names.split("\n")[0:-1]

print()
print("enter to continue if the below sample looks correct. ctrl+c to exit")
print("...")
for i in range(5,15):
    print(names[i])
print("...")
_=input()

results = []


#resp = requests.get('http://go.to', 
#                    proxies=dict(http='socks5://user:pass@host:port',
#                                 https='socks5://user:pass@host:port'))


for idx, name in enumerate(names):
    url = "https://api.genderize.io/?name=" + name
    requ = requests.get(url)
    data = json.loads(requ.content)
    results.append(data)
    print("stole", idx+1, "of", len(names), "got data for name:", name)

# seapie()

with open("result_" + partnum + ".makejson", "w") as file:
    for json in results:
        _ = file.write(str(json)+"\n")
        print("saved data from name:", json["name"])




