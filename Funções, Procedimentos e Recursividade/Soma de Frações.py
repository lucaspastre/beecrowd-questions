def mdc_euclides(a, b):
    resto = a % b
    while resto != 0:
        a = b
        b = resto
        resto = a % b
    return b

def soma(a, b, c, d):
    divisor1 = b * d
    dividendo1 = (a*d) + (b*c)

    divisor2 = (divisor1 // mdc_euclides(divisor1, dividendo1))
    dividendo2 = (dividendo1 // mdc_euclides(divisor1, dividendo1))

    return dividendo2, divisor2

a, b, c, d = map(int, input().split())

numerador, denominador = soma(a, b, c, d)

print(f'{numerador} {denominador}')
