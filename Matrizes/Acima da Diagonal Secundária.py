o = input()
mat = [None] * 12
for i in range(0, 12):
    mat[i] = [None] * 12

for i in range(0, 12):
    for j in range(0, 12):
        mat[i][j] = float(input())

soma = 0
qtd = (144-12)/2
for i in range(0, 12):
    for j in range(0, 12-(i+1)):
        soma += mat[i][j]

if o == 'S':
    print(f'{soma:.1f}')
else:
    print(f'{soma/qtd:.1f}')
