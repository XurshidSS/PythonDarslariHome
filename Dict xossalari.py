""" Dict xossalari """
# dict bu - tartiblangan
# elementlar takrorlanmaydi
# element -> {key: value}
shaxs = {
    "ism": "Xurshid",
    "yoshi": 40,
    "kasbi": "O'qituvchi"
}
print(shaxs)

# elemenmtlarga murojaat qilish
shaxs = {
    "ism": "Xurshid",
    "yoshi": 40,
    "kasbi": "O'qituvchi"
}

# 1-usul.
print(shaxs["ism"])

# 2-usul. get() metodi bilan
print(shaxs.get("ism"))

""" keys() metodi faqatgina kalit so'zlarni chiqaradi. """
shaxs = {
    "ism": "Xurshid",
    "yoshi": 40,
    "kasbi": "O'qituvchi"
}
print(shaxs.keys())

# values() metodi faqatgina qiymatlarni chiqaradi.
shaxs = {
    "ism": "Xurshid",
    "yoshi": 40,
    "kasbi": "O'qituvchi"
}
print(shaxs.values())

""" element qo'shish """
shaxs = {
    "ism": "Xurshid",
    "yoshi": 40,
    "kasbi": "O'qituvchi"
}

shaxs["millati"] = "O'zbek"

print(shaxs)

# update() yordamida bir nechta element qo'shish mumkin.
shaxs.update({"manzili": "Jizzax", "tel": "+99 891 591 77 31"})

print(shaxs)

""" elementni o'zgartirish """
shaxs = {
    "ism": "Xurshid",
    "yoshi": 40,
    "kasbi": "O'qituvchi"
}
shaxs["ism"] = "Oybek"

print(shaxs)

""" elementni o'chirish """
shaxs = {
    "ism": "Xurshid",
    "yoshi": 40,
    "kasbi": "O'qituvchi",
    "millati": "O'zbek"
}

# pop() -> dict.pop(any key)
# dict - lug'at, any - har (lyuboy), key - kalit
shaxs.pop("millati")
print(shaxs)

# popitem() -> bu dictni oxirgi elementini o'chiradi.
# popitem() no parametr
shaxs = {
    "ism": "Xurshid",
    "yoshi": 40,
    "kasbi": "O'qituvchi",
    "millati": "O'zbek"
}

shaxs.popitem()
print(shaxs)

# clear() bu tozalash
shaxs = {
    "ism": "Oybek",
    "yoshi": 20,
    "kasbi": "O'qituvchi",
    "millati": "O'zbek"
}

shaxs.clear()
print(shaxs)

# del -> del dict[key] - bunda keyga mos element o'chib ketadi.
# del -> del dict - bu dictni o'zini xotiradan o'chiradi.
shaxs = {
    "ism": "Xurshid",
    "yoshi": 40,
    "kasbi": "O'qituvchi",
    "millati": "O'zbek"
}

del shaxs["yoshi"]
print(shaxs)

del shaxs
# barchasi xotiradan o'chdi.
# agar print(shaxs) buyruq berilsa, qip-qizil xato chiqaradi.