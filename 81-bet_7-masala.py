a = int(input("a = "))
b = int(input("b = "))

if a > 0 and b > 0 and a + b > 100:
    print(f"a / b = {a / b}")
elif a + b < 100:
    print(f"a * b = {a * b}")