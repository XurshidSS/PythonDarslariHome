n = int(input("n = "))
k = str(n)
juft = 0
for i in range(len(k)):
    if i % 2 == 0:
        juft += 1
print(juft)