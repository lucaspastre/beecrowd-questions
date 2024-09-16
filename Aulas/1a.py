n = input().split()  # recebe valores e armazena no vetor
for i in range(0, len(n)):
    n[i] = int(n[i])  # converte cada elemento para inteiro
    n[i] = n[i] * 3  # multiplica cada elemento por 3

for i in range(0, len(n)-1):  # imprime todos os elementos menos o ultimo, separados por espaço
    print(f'{n[i]}', end=' ')
print(f'{n[len(n)-1]}')  # imprime o ultimo elemento do vetor
