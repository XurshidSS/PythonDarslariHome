n = int(input("n = "))

def rim(a):
    txt = ''
    if a // 100 > 0:
        k = a // 100
        txt += k * 'C'
    if a // 10 % 10 >= 0:
        k = a // 10 % 10
        if k <= 3:
            txt += k * 'X'
        elif k == 4:
            txt += 'XL'
        elif k >= 5 and k < 9:
            txt += 'L' + (k - 5) * 'X'
        elif k == 9:
            txt += 'XC'
    if a % 10 > 0:
        v = a % 10
        if v < 4:
            txt += 'I' * v
        elif v == 4:
            txt += 'IV'
        elif v < 9 and v > 4:
            txt += "V" + (v - 5) * "I"
        elif v == 9:
            txt += "IX"
    print(txt)


rim(n)