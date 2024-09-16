a = int(input())
feliz_natal = {}

for i in range(0, a):
    idioma = input()
    parabens = input()
    feliz_natal[idioma] = parabens

b = int(input())

for i in range(0, b):
    nome = input()
    lingua = input()

    print(nome)
    print(feliz_natal[lingua])
    print()
