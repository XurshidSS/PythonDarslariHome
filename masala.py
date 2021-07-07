
a = int(input("Birinchi son: "))
b = int(input("Ikkinchi son: "))
while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a
EKUB = a + b
a = int(input("Birinchi son: "))
b = int(input("Ikkinchi son: "))
EKUK = a * b / EKUB

print(f"EKUK = {EKUK}")
