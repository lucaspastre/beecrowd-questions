while True:
    try:
        A, B, C = map(int, input().split())

        if A != B and A != C:
            print('A')

        elif A == B == C:
            print('*')

        elif B != A and B != C:
            print('B')

        else:
            print('C')

    except EOFError:
        break
