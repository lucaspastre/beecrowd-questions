while True:
    try:
        a, b, c = input().split()
        a = int(a)
        b = int(b)
        c = int(c)

        p = (a + b + c) / 2
        area_triangulo = (p*(p-a)*(p-b)*(p-c))**(1/2)

        r1 = (2*area_triangulo) / (a+b+c)
        area_rosas = 3.1415926535897*(r1**2)

        area_violeta = area_triangulo - area_rosas

        r2 = (a*b*c) / (4*area_triangulo)
        area_girassol = 3.1415926535897*(r2**2) - area_triangulo

        print(f'{area_girassol:.4f}', end=' ')
        print(f'{area_violeta:.4f}', end=' ')
        print(f'{area_rosas:.4f}')

    except EOFError:
        break
