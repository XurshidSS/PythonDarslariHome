# 2 - misol. Button (tugma)
from tkinter import *

asosiyOyna = Tk()

# oynani o'lchamini belgilash uchun
asosiyOyna.geometry('600x400')

# tugma qo'shish
# Button(oyna, text="matn", bd="qalinligi", command="tugma bosilgandagi hodisa")
tugma = Button(asosiyOyna, text="Yopish", bd="10", command=asosiyOyna.destroy)

# buttonni oynaga joylash
tugma.pack()

asosiyOyna.mainloop()