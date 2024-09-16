


while True:
    try:
        a, b = input().split()
        a = int(a)
        b = int(b)

        mat = [None] * a
        result = [None] * a
        for i in range(0, a):
            result[i] = [None] * b

        for i in range(0, a):
            mat[i] = input().split()
            for j in range(0, b):
                mat[i][j] = int(mat[i][j])
                result[i][j] = 0

        for i in range(0, a):
            for j in range(0, b):
                if mat[i][j] == 1:
                    result[i][j] = 9
                else:
                    vizinho_i = i-1  # Acima
                    vizinho_j = j
                    if vizinho_i >= 0 and mat[vizinho_i][vizinho_j] == 1:
                        result[i][j] += 1
                    vizinho_i = i+1  # Abaixo
                    vizinho_j = j
                    if vizinho_i < a and mat[vizinho_i][vizinho_j] == 1:
                        result[i][j] += 1
                    vizinho_i = i      # Esquerda
                    vizinho_j = j-1
                    if vizinho_j >= 0 and mat[vizinho_i][vizinho_j] == 1:
                        result[i][j] += 1
                    vizinho_i = i          # Direita
                    vizinho_j = j+1
                    if vizinho_j < b and mat[vizinho_j][vizinho_j] == 1:
                        result[i][j] += 1

        for i in range(0, a):
            for j in range(0, b):
                print('%2d' % result[i][j], end='')
            print("")
        print()

    except EOFError:
        break



