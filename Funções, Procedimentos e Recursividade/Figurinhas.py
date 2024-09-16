def mdc(maior, menor):
    resto = maior % menor
    while resto != 0:
        maior = menor
        menor = resto
        resto = maior % menor
    return menor

teste = int(input())
for i in range(teste):
    a, b = input().split()
    a = int(a)
    b = int(b)

    if a == b:
        maior = menor = a
    elif a > b:
        maior = a
        menor = b
    elif b > a:
        maior = b
        menor = a

    print(mdc(maior, menor))
