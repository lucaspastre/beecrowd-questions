while True:
    n = int(input())
    if n == 0:
        break
    r = (n*(n+1)*(2*n+1))/6
    print(f'{r:.0f}')
