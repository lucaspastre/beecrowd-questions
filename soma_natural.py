a, b = map(int, (input().split()))
# s é a soma dos numeros da pa e n é a formula geral da pa isolando n (numero de termos)
n = b-a+1
s = ((a+b)*n)/2
print('%d' % s)
