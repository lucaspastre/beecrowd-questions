o, b, i = map(float, input().split())

if o < b and o < i:
    print('Otavio')

elif b < o and b < i:
    print('Bruno')

elif i < b and i < o:
    print('Ian')

elif o == b or b == i or o == i:
    print('Empate')
