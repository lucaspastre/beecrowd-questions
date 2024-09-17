N1, D1, V1 = map(int, input().split())
N2, D2, V2 = map(int, input().split())
t1 = D1/V1
t2 = D2/V2
if t1 > t2:
    print('%d' % N2)

else:
    print('%d' % N1)
