a, b = map(int, input().split())

if a == 1:
    print('Total: R$ %.2f' % (b * 4))

elif a == 2:
    print('Total: R$ %.2f' % (b * 4.50))

elif a == 3:
    print('Total: R$ %.2f' % (b * 5))

elif a == 4:
    print('Total: R$ %.2f' % (b * 2))

else:
    print('Total: R$ %.2f' % (b * 1.50))
