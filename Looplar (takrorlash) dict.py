""" loop lar (takrorlash) """

shaxs = {
    "ism": "Oybek",
    "yoshi": 20,
    "kasbi": "O'qituvchi",
    "millati": "O'zbek"
}

for i in shaxs: # bu yerda i -> keylar
    print(i) # bunda keylar chiqadi

for i in shaxs:
    print(shaxs[i]) # bunda value lar chiqadi

for i in shaxs:
    print(shaxs.get(i)) # bunda ham value lar chiqadi

for i in shaxs.keys():
    print(i) # bunda keylar chiqadi

for i in shaxs.values():
    print(i) # bunda ham value lar chiqadi

for x, y in shaxs.items():
    print(x, y)

""" copy() dict.copy() no parameter"""
shaxs = {
    "ism": "Oybek",
    "yoshi": 20,
    "kasbi": "O'qituvchi",
    "millati": "O'zbek"
}

shaxs1 = shaxs.copy()
shaxs2 = shaxs

shaxs.clear()

print("sh1", shaxs1)
print("sh2", shaxs2)

""" Joylashtirilgan lug'at """

oila = {
    "ota": {
        "ism": "John",
        "yoshi": 24
    },
    "ona": {
        "ism": "Anna",
        "yoshi": 20
    },
    "bola": {
        "ismi": "Jack",
        "yoshi": 2
    }
}

# bolani ismini chiqarish
print(oila.get("bola").get("ismi"))
print(oila["bola"]["ismi"])

for azo in oila:
    if azo == "bola":
        for i in oila[azo]:
            if i == "ismi":
                print(oila[azo][i])

