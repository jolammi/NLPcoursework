names = {}

__data__ = []
with open("names.csv", "r") as file:
    _ = file.read()
__data__.extend(_.split("\n")[0:-1])
with open("longnames.csv", "r") as file:
    _ = file.read()
__data__.extend(_.split("\n")[0:-1])
for line in __data__:
    name, sex = line.split(",")
    names[name] = int(sex)
