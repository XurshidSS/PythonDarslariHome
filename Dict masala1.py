# 1 - masala yoshi degan key bormi yo'qmi
talaba = {
    "ism": "Oybek",
    "yoshi": 22,
}

yil = int(input("necha yil o'tdi -> "))
talaba["yoshi"] = talaba["yoshi"] + yil
print(talaba)

for i in talaba:
    if i == "yosh":
        print("bor")
        break
else:
    print("yo'q")