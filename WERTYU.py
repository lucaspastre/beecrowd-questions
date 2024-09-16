n = input().upper()
n = list(n.split())
lista = ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=',
         'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']', "\\",
         'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', "'",
         'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/']

for i in range(0, len(n)):
    n[i] = list(n[i])
    for a in range(0, len(n[i])):
        pos = lista.index(n[i][a])
        if n[i][a] == 'A' or n[i][a] == 'Z' or n[i][a] == 'Q' or n[i][a] == '`':
            print(lista[pos], end='')
        else:
            print(lista[pos-1], end='')
    if i < len(n)-1:
        print('', end=' ')
    else:
        print('')
