from seapie import Seapie as seapie

good = []
bad = []


for num in range(1,111):
    num = str(num)
    with open("result_" + num + ".makejson", "r") as file:
        data = file.read()
        data = data.split("\n")[0:-1]
        for json in data:
            parsed = eval(json)
            gender = parsed["gender"]
            if gender is not None:
                if gender == "male":
                    good.append((parsed["name"],1))
                elif gender == "female":
                    good.append((parsed["name"],2))
                else:
                    raise AssertionError
            else:
                bad.append((parsed["name"], 0))


with open("names2.csv", "w") as file:
    for name, sex in good:
        _ = file.write(name+","+str(sex)+"\n")


with open("unknown.csv", "w") as file:
    for name, sex in bad:
        _ = file.write(name+","+str(sex)+"\n")

seapie()





