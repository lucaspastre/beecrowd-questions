cont = 0
while True:
    n = int(input())

    if n == 0:
        break

    cont += 1
    print(f'Teste {cont}')
    a = n//50
    b = (n % 50)//10
    c = ((n % 50) % 10)//5
    d = (((n % 50) % 10) % 5)//1
    print(f'{a} {b} {c} {d}')
    print()
