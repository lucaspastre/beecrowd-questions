t = int(input())
cont = 0
for i in range(0, t):
    cont += 1
    n = input().split()
    qtd = int(n[0])
    n2 = (qtd//2)+1
    print(f'Case {cont}: {n[n2]}')
