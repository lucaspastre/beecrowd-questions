while True:
    try:
        lista = []
        n = int(input())
        for i in range(n):
            code = input().split()
            lista.append(code)

            lista.sort()

        for i in range(0, len(lista)):
            print("".join(lista[i]))
    except EOFError:
        break
