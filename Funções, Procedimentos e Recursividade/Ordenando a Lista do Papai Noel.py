n = int(input())
comportaram = 0
n_comportaram = 0
lista = []

for i in range(n):
    nome = input().split()
    lista.append(nome[1])
    lista.sort()

    if nome[0] == '+':
        comportaram += 1
    else:
        n_comportaram += 1

for i in range(0, len(lista)):
    print("".join(lista[i]))

print(f'Se comportaram: {comportaram} | Nao se comportaram: {n_comportaram}')
