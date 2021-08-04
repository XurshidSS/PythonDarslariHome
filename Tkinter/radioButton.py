# radio button
from tkinter import *

# asosiy oynani yasash
asosiyOyna = Tk()

# o'lcham berish
asosiyOyna.geometry('400x400')

# string ma'lumotlardan foydalanish uchun
v = StringVar(asosiyOyna, '1')

# tugmalar qiymatlarini saqlash uchun lug'at
qiymatlar = {
    'RadioButton 1': "1",
    'RadioButton 2': "2",
    'RadioButton 3': "3",
    'RadioButton 4': "4",
    'RadioButton 5': "5"
}

# barcha tugamalarni Asosiy oynaga joylash uchun for loop
for (matn, qiymat) in qiymatlar.items():
    # radio button qurish:
    tugma = Radiobutton(
        asosiyOyna,
        text=matn,
        variable=v,
        value=qiymat,
        indicator=0,
        background="light blue"
    )
    #     pack(x kordinata, y kordinata)
    tugma.pack(ipadx=100, ipady=20)

# oynani ushlab turish uchun
asosiyOyna.mainloop()



# Masala.
"""  radio button erkak va ayol uchun """
from tkinter import *

# asosiy oynani yasash
asosiyOyna = Tk()

# o'lcham berish
asosiyOyna.geometry('400x400')

# string ma'lumotlardan foydalanish uchun
v = StringVar(asosiyOyna, '1')

# tugmalar qiymatlarini saqlash uchun lug'at
qiymatlar = {
    'Erkak': "1",
    'Ayol': "2"
}

# barcha tugamalarni Asosiy oynaga joylash uchun for loop
for (matn, qiymat) in qiymatlar.items():
    # radio button qurish:
    tugma = Radiobutton(
        asosiyOyna,
        text=matn,
        variable=v,
        value=qiymat,
        indicator=0,
        background="light blue"
    )
    #     pack(x kordinata, y kordinata)
    tugma.pack(ipadx=100, ipady=20)

# oynani ushlab turish uchun
asosiyOyna.mainloop()