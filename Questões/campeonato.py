A, B, C, D, E, F = map(int, input().split())

if A*3+B > D*3+E:
    print('C')

elif A*3+B < D*3+E:
    print('F')

else:
    if C > F:
        print('C')
    elif F > C:
        print('F')
    else:
        print('=')
