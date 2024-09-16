while True:
    try:
        d, vf, vg = map(int, input().split())

        distancia_guarda = (144+d**2)**(1/2)

        if vf > 0 and vg == 0:
            print('N')
        elif vg > 0 and vf == 0:
            print('S')
        elif vg == 0 and vf == 0:
            print('S')
        elif (12 / vf) >= (distancia_guarda / vg):
            print('S')
        else:
            print('N')

    except EOFError:
        break
