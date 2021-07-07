son = int(input("son = "))
a = son
xonalarSoni = 1
while True:
    a = a // 10
    if a != 0:
        xonalarSoni += 1
    else:
        break
teskariSon = 0
a = son
xonaIndeksi = 0
while True:
    teskariSon += a // (10 ** (xonalarSoni - 1)) % 10 * (10 ** xonaIndeksi)
    xonaIndeksi += 1
    xonalarSoni -= 1
    if xonalarSoni == 0:
        break
if son == teskariSon:
    print("polidrom")
else:
    print("polidrom emas")