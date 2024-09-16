last = False
while True:
    try:
        ano = int(input())
        if last:
            print()

        if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
            print('This is leap year.')
            if ano % 15 == 0:
                print('This is huluculu festival year.')
            if ano % 55 == 0:
                print('This is bulukulu festival year.')

        elif ano % 15 == 0:
            print('This is huluculu festival year.')

        else:
            print('This is an ordinary year.')

        last = True
    except EOFError:
        break
