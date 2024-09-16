def mdc(a, b):
    resto = a % b
    while resto != 0:
        a = b
        b = resto
        resto = a % b
    return b

def mdc2(a, b, c):
    d = mdc(a, b)
    resto = d % c
    while resto != 0:
        d = b
        b = resto
        resto = d % b
    return b

def pitagoras(a, b, c):
    pit = False
    if a**2 == b**2 + c**2:
        pit = True
    return pit

while True:
    try:
        n0, n1, n2 = input().split()
        n0 = int(n0)
        n1 = int(n1)
        n2 = int(n2)

        if pitagoras(n0, n1, n2) or pitagoras(n1, n2, n0) or pitagoras(n2, n1, n0) is True:
            if mdc2(n0, n1, n2) == 1:
                print('tripla pitagorica primitiva')
            else:
                print('tripla pitagorica')
        else:
            print('tripla')

    except EOFError:
        break
