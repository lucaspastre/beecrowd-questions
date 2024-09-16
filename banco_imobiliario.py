a, b = input().split()
a = int(a)
b = int(b)
Dalia = Eloi = Felix = a

for i in range(0, b):
    n = input().split()

    if n[0] == 'C':
        if n[1] == 'D':
            Dalia -= int(n[2])
        elif n[1] == 'E':
            Eloi -= int(n[2])
        else:
            Felix -= int(n[2])
    elif n[0] == 'V':
        if n[1] == 'D':
            Dalia += int(n[2])
        elif n[1] == 'E':
            Eloi += int(n[2])
        else:
            Felix += int(n[2])
    else:
        if n[1] == 'D':
            if n[2] == 'E':
                Dalia += int(n[3])
                Eloi -= int(n[3])
            else:
                Dalia += int(n[3])
                Felix -= int(n[3])
        elif n[1] == 'E':
            if n[2] == 'D':
                Eloi += int(n[3])
                Dalia -= int(n[3])
            else:
                Eloi += int(n[3])
                Felix -= int(n[3])
        else:
            if n[2] == 'D':
                Felix += int(n[3])
                Dalia -= int(n[3])
            else:
                Felix += int(n[3])
                Eloi -= int(n[3])

print(Dalia, end=" ")
print(Eloi, end=" ")
print(Felix)
