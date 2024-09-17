posicao = 0
maior = 0

for _ in range(1, 101):
    n = int(input())

    if n > maior:
        maior = n
        posicao = _

print(maior)
print(posicao)
