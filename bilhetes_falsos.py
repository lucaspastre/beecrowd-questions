while True:
    originais, pessoas = map(int, input().split())
    if originais == pessoas == 0:
        break

    bilhetes = input().split()
    lista = []
    cont = 0

    if pessoas > originais:
        print(pessoas - originais)

    else:
        for i in range(len(bilhetes)):
            if bilhetes[i] in lista:
                cont += 1

            lista.append(bilhetes[i])

        print(cont)
