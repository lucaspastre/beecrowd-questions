c = int(input())
for i in range(0, c):
    n = input().split()
    qtd = int(n[0])
    soma = 0
    cont = 0

    for i2 in range(1, len(n)):
        n[i2] = int(n[i2])
        soma += n[i2]
    media = soma / qtd

    for i2 in range(1, len(n)):
        if n[i2] > media:
            cont += 1
    percentual = (cont*100)/qtd

    print(f'{percentual:.3f}%')
