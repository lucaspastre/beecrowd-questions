N = int(input())
for _ in range(1, N+1):
    X, Y = map(int, input().split())

    r = (3*X)**2 + Y**2
    b = 2*X**2 + (5*Y)**2
    c = -100*X + Y**3

    if r > b and r > c:
        print('Rafael ganhou')

    elif b > r and b > c:
        print('Beto ganhou')

    else:
        print('Carlos ganhou')
