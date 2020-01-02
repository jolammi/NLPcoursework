import requests
import json
import sys
from seapie import Seapie as seapie
import random
import atexit


def save():
    """save progress to file at exit"""
    try:
        with open("result_" + partnum + ".makejson", "w") as file:
            for idx, json in enumerate(results):
                _ = file.write(str(json)+"\n")
                print(idx+1, "saved data from name:", json["name"])
    except Exception:
        print("DATAN DUMPPAUKSESSA KÄVI PERKELE JOTAIN. SEAPIE AUKI")
        seapie()
atexit.register(save)


# get part file number and load it
partnum = sys.argv[1]
with open("part_" + partnum + ".csv", "r") as file:
    names = file.read()
names = names.split("\n")[0:-1]


# preview part
print()
print("enter to continue if the below sample looks correct. ctrl+c to exit")
print("...")
for i in range(5,15):
    print(names[i])
print("...")
_=input()


# initialize proxies
counter = 0
with open("proxylist.txt", "r") as file:
    myproxies = file.read().split("\n")
choice = myproxies[counter]
counter +=1
myproxy = dict(http="socks5://"+choice,https="socks5://"+choice)
if counter == len(myproxies):
    counter = 0


# main loop
results = []
for idx, name in enumerate(names):
    while True:
        try:
            url = "http://api.genderize.io/?name=" + name
            requ = requests.get(url, proxies=myproxy)
            data = json.loads(requ.content)
            
            if data == {'error': 'Request limit reached'}:
                raise AssertionError
            
            results.append(data)
            print("stole", idx+1, "of", len(names), "got data for name:", name, "with", choice)
        except KeyboardInterrupt:
            seapie()
        except Exception:
            print("vitun proxy kaatui", choice)
            #import traceback
            #traceback.print_exc()
            #seapie()
            
            with open("proxylist.txt", "r") as file:
                myproxies = file.read().split("\n")
            choice = myproxies[counter]
            counter +=1
            myproxy = dict(http="socks5://"+choice,https="socks5://"+choice)
            if counter == len(myproxies):
                counter = 0
        else: # if error did not happen move to next item
            break
