from seapie import Seapie as seapie

with open("important_good4_manual.csv", "r") as file:
    data = file.read()
data = data.split("\n")[0:-1]
abc = "abcedfghijklmnopqrstuvwxyz '"
names = []
parsed = []

for line in data:
    for chr in line:
        if chr not in abc:
            raise AssertionError
    if " " in line:
        names.extend(line.split(" "))
    else:
        names.append(line)
names = sorted(list(set(names)))


for name in names:
    if len(name) == 1:
        continue
    elif len(name) == 2 and name[0] == name[1]:
        continue
    else:
        parsed.append(name)
        
 
parsed = sorted(list(set(parsed)))
print(len(parsed))


idx = 0
while parsed:
    idx += 1
    with open("./final/part_"+str(idx)+".csv", "w") as file:
        for i in range(900):
            try:
                file.write(parsed.pop(0)+"\n")
                print(idx)
            except IndexError:
                pass

seapie()





