a = int(input("Birinchi son: "))
b = int(input("Birinchi son: "))
while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a
EKUB = a + b
print(f"EKUB = {EKUB}")