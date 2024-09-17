while True:
    n = input().split()
    n = list(n)
    letra = 0
    r = 'Y'
    if n[0] == '*':
        break

    for i in range(0, len(n)):
        n[i] = n[i].upper()

        for i2 in range(0, len(n[i])):
            letra = n[0][0]

            if n[i][0] != letra:
                r = 'N'
    print(r)
