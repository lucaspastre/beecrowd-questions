c = int(input())

mat = [None] * 3
for i in range(0, 3):
    mat[i] = input().split()
    for j in range(0, 3):
        mat[i][j] = int(mat[i][j])

soma = 0

for i in range(0, 3):
    soma += mat[i][c]

print(soma)
