a, b, c = map(int, input().split())

if a > b > c:
    print('%d' % b)

elif a > c > b:
    print('%d' % c)

elif b > a > c:
    print('%d' % a)

elif b > c > a:
    print('%d' % c)

elif c > a > b:
    print('%d' % a)

else:
    print('%d' % b)
