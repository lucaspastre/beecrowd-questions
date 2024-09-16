num = int(input())
p = input().split()
cont1 = 0
cont0 = 0
for i in range(0, len(p)):
    p[i] = int(p[i])
    if p[i] == 1:
        cont1 += 1
    elif p[i] == 0:
        cont0 += 1

if cont1 >= cont0:
    print('N')
else:
    print('Y')
