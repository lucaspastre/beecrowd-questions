A, B, C = map(int, input().split())

if B-C < A < B+C:
    if A == B and B == C and A == C:
        if A**2 == B**2+C**2:
            print('Valido-Equilatero\nRetangulo: S')
        else:
            print('Valido-Equilatero\nRetangulo: N')
    elif A != B and B != C and A != C:
        if A**2 == B**2+C**2:
            print('Valido-Escaleno\nRetangulo: S')
        else:
            print('Valido-Escaleno\nRetangulo: N')
    else:
        if A**2 == B**2+C**2:
            print('Valido-Isoceles\nRetangulo: S')
        else:
            print('Valido-Isoceles\nRetangulo: N')

else:
    print('Invalido')
