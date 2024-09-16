import math

cont = 0
while True:
    estradas, inteiros = input().split()
    estradas = int(estradas)
    inteiros = int(inteiros)
    cont += 1

    if estradas == 0 and inteiros == 0:
        break

    if math.ceil((estradas-inteiros)/inteiros) > 26:
        print(f'Case {cont}: impossible')

    else:
        if estradas == inteiros or inteiros > estradas:
            print(f'Case {cont}: 0')

        elif estradas < 2 * inteiros:
            print(f'Case {cont}: 1')

        else:
            print(f'Case {cont}: {(estradas-1)//inteiros}')
