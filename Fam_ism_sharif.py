name = str(input("name = "))
grandFatherName = str(input("grandFatherName = "))
fatherName = str(input("fatherName = "))
jinsi = str(input("jinsi = "))
if jinsi == "erkak":
    if grandFatherName[-1] == "e" or "u" or "i" or "o" or "a":
        grandFatherName = grandFatherName + "yev"
    else:
        grandFatherName = grandFatherName + "ov"
    if fatherName[-1] == "e" or "u" or "i" or "o" or "a":
        fatherName = fatherName + "yevich"
    else:
        fatherName = fatherName + "ovich"
print(grandFatherName + " " + name + " " + fatherName)
if jinsi == "ayol":
    grandFatherName = grandFatherName + "ova"
    fatherName = fatherName + "ovna"
    print(grandFatherName + " " + name + " " + fatherName)