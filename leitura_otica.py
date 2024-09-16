while True:
    n = int(input())

    if n == 0:
        break

    for _ in range(1, n+1):
        a, b, c, d, e = map(int, input().split())
        if (a <= 127) and b > 127 and c > 127 and d > 127 and e > 127:
            print('A')

        elif (b <= 127) and a > 127 and c > 127 and d > 127 and e > 127:
            print('B')

        elif (c <= 127) and a > 127 and b > 127 and d > 127 and e > 127:
            print('C')

        elif (d <= 127) and a > 127 and b > 127 and c > 127 and e > 127:
            print('D')

        elif (e <= 127) and a > 127 and b > 127 and c > 127 and d > 127:
            print('E')

        else:
            print('*')
