n = int(input())
dicionario = {}

for a in range(0, n):
    m = int(input())
    for i in range(0, m):
        fruta, valor = input().split()

        dicionario[fruta] = float(valor)

    p = int(input())
    preco = 0
    for j in range(0, p):
        frutatipo, quantidade = input().split()
        quantidade = int(quantidade)

        preco += dicionario[frutatipo] * quantidade

    print(f'R$ {preco:.2f}')