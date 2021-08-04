from tkinter import *

asosiyOyna = Tk()

# oynani o'lchamini belgilash uchun
asosiyOyna.geometry('600x400')

# tugma qo'shish
tugma = Button(asosiyOyna, text="Tanlang")

# buttonni oynaga joylash
tugma.pack()
asosiyOyna.mainloop()