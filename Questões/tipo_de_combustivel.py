n = 0
a = 0
g = 0
d = 0
while n != 4:
    n = int(input())
    if n > 4 or n < 1:
        n = 0

    if n == 1:
        a = a+1

    elif n == 2:
        g = g+1

    elif n == 3:
        d = d+1

print(f'MUITO OBRIGADO\nAlcool: {a}\nGasolina: {g}\nDiesel: {d}')
