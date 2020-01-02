from seapie import Seapie as seapie

good = []
bad = []


for num in "123456789":
    with open("result_" + num + ".makejson", "r") as file:
        data = file.read()
        data = data.split("\n")[0:-1]
        for json in data:
            parsed = eval(json)
            if parsed["gender"] is not None:
                good.append(parsed["name"])
            else:
                bad.append(parsed["name"])
            
            
abc = "abcedfghijklmnopqrstuvwxyz"


seapie()





