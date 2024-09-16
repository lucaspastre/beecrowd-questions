def frequencia(a, lista):
    cont = 0
    for num in lista:
        if num == a:
            cont += 1
    return cont

casos = int(input())
lista = []
verificados = []

for i in range(casos):
    num = int(input())
    lista.append(num)

lista.sort()

for j in range(len(lista)):
    if lista[j] not in verificados:
        qtd = frequencia(lista[j], lista)
        verificados.append(lista[j])
        print(f'{lista[j]} aparece {qtd} vez(es)')
