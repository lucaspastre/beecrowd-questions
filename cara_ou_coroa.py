while True:
    n = int(input())
    if n == 0:
        break

    maria = 0
    joao = 0
    lista = input().split()

    for i in range(0, n):
        lista[i] = int(lista[i])

        if lista[i] == 0:
            maria += 1

        elif lista[i] == 1:
            joao += 1

    print(f'Mary won {maria} times and John won {joao} times')
