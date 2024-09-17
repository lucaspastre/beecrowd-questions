n = int(input())

for i in range(n):
    lista = []
    a = int(input())
    b, c, d, e = map(int, input().split())
    f = int(input())
    lista.append(a)
    lista.append(b)
    lista.append(c)
    lista.append(d)
    lista.append(e)
    lista.append(f)

    if lista.count(a) < 2 and lista.count(b) < 2 and lista.count(c) < 2 and lista.count(d) < 2 and lista.count(e) < 2 and lista.count(f) < 2:
        if (a + f == 7) and (b + d == 7) and (c + e == 7):
            if a != 0 and b != 0 and c != 0 and d != 0 and e != 0 and f != 0:
                if a > 0 and b > 0 and c > 0 and d > 0 and e > 0 and f > 0:
                    print('SIM')
                else:
                    print('NAO')
            else:
                print('NAO')
        else:
            print('NAO')
    else:
        print('NAO')
