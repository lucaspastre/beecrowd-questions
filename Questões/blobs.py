n = int(input())
for i in range(n):
    cont = 0
    comida = float(input())

    while comida > 1:
        comida = comida*0.5
        cont += 1

    print(f'{cont} dias')
