from datetime import datetime

while True:
    try:
        mes, dia = map(int, input().split())
        natal = datetime(2016, 12, 25)
        data = datetime(2016, mes, dia)
        diferenca = (natal - data).days

        if dia == 24 and mes == 12:
            print('E vespera de natal!')

        elif dia == 25 and mes == 12:
            print('E natal!')

        elif dia > 25 and mes == 12:
            print('Ja passou!')

        else:
            print(f'Faltam {diferenca} dias para o natal!')

    except EOFError:
        break