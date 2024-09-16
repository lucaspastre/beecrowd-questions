n = int(input())
for i in range(n):
    senha = input().split()
    cont = 0
    for j in range(0, len(senha)):
        for k in range(0, len(senha[j])):
            cont += 1
            if cont == 12:
                break

            if senha[j][k] in ('G', 'Q', 'a', 'k', 'u'):
                print('0', end='')

            if senha[j][k] in ('I', 'S', 'b', 'l', 'v'):
                print('1', end='')

            if senha[j][k] in ('E', 'O', 'Y', 'c', 'm', 'w'):
                print('2', end='')

            if senha[j][k] in ('F', 'P', 'Z', 'd', 'n', 'x'):
                print('3', end='')

            if senha[j][k] in ('J', 'T', 'e', 'o', 'y'):
                print('4', end='')

            if senha[j][k] in ('D', 'N', 'X', 'f', 'p', 'z'):
                print('5', end='')

            if senha[j][k] in ('A', 'K', 'U', 'g', 'q'):
                print('6', end='')

            if senha[j][k] in ('C', 'M', 'W', 'h', 'r'):
                print('7', end='')

            if senha[j][k] in ('B', 'L', 'V', 'i', 's'):
                print('8', end='')

            if senha[j][k] in ('H', 'R', 'j', 't'):
                print('9', end='')

