n = int(input())
for i in range(n):
    primeiro, segundo = input().split()
    tamanho_segundo = len(segundo)
    ultimo = primeiro[-tamanho_segundo:]

    if ultimo == segundo:
        print('encaixa')
    else:
        print('nao encaixa')

