def iccanobif(n, dicionario={}):
    if n in dicionario:
        return dicionario[n]

    if n <= 1:
        return n

    resultado = iccanobif(n-1, dicionario) + iccanobif(n-2, dicionario)
    dicionario[n] = resultado
    return resultado

n = int(input())
for i in range(n, 0, -1):
    if i != 1:
        print(iccanobif(i), end=' ')
    else:
        print(iccanobif(i), end='')
