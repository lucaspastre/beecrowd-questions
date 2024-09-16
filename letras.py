letra = input()
texto = input().split()
cont = 0

for i in range(0, len(texto)):
    lista = []
    for j in range(0, len(texto[i])):
        if letra not in lista:
            lista.append(texto[i][j])

            if letra in lista:
                cont += 1

porcentagem = (cont / len(texto)) * 100

print(f'{porcentagem:.1f}')
