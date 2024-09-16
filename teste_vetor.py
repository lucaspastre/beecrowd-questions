v = input().split()

soma = 0
for i in range(0, len(v)):
    soma += int(v[i])

print(f'{soma/len(v):.2f}')


