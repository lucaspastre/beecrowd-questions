cont = 0
while True:
    n = int(input())
    if n == 0:
        break
    cont += 1
    somaj = somaz = 0
    print(f'Teste {cont}')
    for i in range(0, n):
        j, z = map(int, input().split())
        somaj += j
        somaz += z
        dif = somaj-somaz
        print(dif)
    print()


