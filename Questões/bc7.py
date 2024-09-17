a = float(input())
b = float(input())
c = float(input())
m = (a+b+c)/3
if m >= 6:
    print('%.2f - Aprovado' % m)
elif m >=3.5<6:
    print('%.2f - Recuperação' % m)
else:
    print('%.2f - Reprovado' %m)
