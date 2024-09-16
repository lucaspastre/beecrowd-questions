cont = 0

while True:
    cont += 1
    r = int(input())
    s1 = 0
    s2 = 0
    if r == 0:
        break

    for c in range(1, r+1):
        a, b = map(int, input().split())
        s1 += a
        s2 += b

    if s2 > s1:
        print(f'Teste {cont}')
        print('Beto')
        print()

    elif s1 > s2:
        print(f'Teste {cont}')
        print('Aldo')
        print()
