n = int(input())
for i in range(0, n):
    leds = 0
    numero = list(input())
    for digito in numero:
        if digito == '1':
            leds += 2
        elif digito == '2':
            leds += 5
        elif digito == '3':
            leds += 5
        elif digito == '4':
            leds += 4
        elif digito == '5':
            leds += 5
        elif digito == '6':
            leds += 6
        elif digito == '7':
            leds += 3
        elif digito == '8':
            leds += 7
        elif digito == '9':
            leds += 6
        elif digito == '0':
            leds += 6

    print(leds, "leds")
