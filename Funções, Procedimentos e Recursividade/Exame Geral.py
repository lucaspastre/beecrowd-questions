while True:
    try:
        habitantes, consultas = map(int, input().split())
        lista = []
        for i in range(habitantes):
            nota = int(input())
            lista.append(nota)
            lista.sort(reverse=True)

        for j in range(consultas):
            posicao = int(input())
            print(lista[posicao-1])

    except EOFError:
        break
