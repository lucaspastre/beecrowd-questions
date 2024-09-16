nome = input().split()
espacos = len(nome) - 1
cont = 0

for i in range(0, len(nome)):
    for j in range(0, len(nome[i])):
        cont += 1

if (cont + espacos) <= 80:
    print('YES')

else:
    print('NO')
