n = int(input())

for a in range(1, n + 1):
    soma = 0
    x, y = map(int, input().split())

    if x > y:
        x, y = y, x

    if x % 2 == 0:
        x = x+1

    elif x % 2 != 0:
        x = x+2

    for b in range(x, y, 2):
        soma += b

    print(soma)
