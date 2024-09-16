pares = []
impares = []
q = int(input())
for i in range(q):
    numero = int(input())

    if (numero % 2) == 0:
        pares.append(numero)
    else:
        impares.append(numero)

pares.sort()
impares.sort(reverse=True)  #organiza os pares de maneira decrescente

for j in range(0, len(pares)):
    print(pares[j])

for k in range(0, len(impares)):
    print(impares[k])
