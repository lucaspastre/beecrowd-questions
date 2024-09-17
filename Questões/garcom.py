n = int(input())
soma = 0

for a in range(1, n+1):
    l, c = map(int, input().split())

    if l > c:
        soma = soma + c

print(soma)
