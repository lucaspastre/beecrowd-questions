n = int(input())
v = input().split()
menor = int(v[0])
cont = 0

for i in range(0, n):
    v[i] = int(v[i])

    if v[i] < menor:
        cont = i
        menor = v[i]

print(f'Menor valor: {menor}')
print(f'Posicao: {cont}')
