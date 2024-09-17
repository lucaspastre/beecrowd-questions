n, m = input().split()
n = int(n)
m = int(m)
cont = 0

mat = [None] * n
for i in range(0, n):
    mat[i] = input().split()
    for j in range(0, m):
        mat[i][j] = int(mat[i][j])

for i in range(0, n):
    marcou = 1
    for j in range(0, m):
        if mat[i][j] == 0:
            marcou = 0
            break
    cont += marcou

print(cont)
