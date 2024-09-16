while True:
    d, n = input().split()

    if d == '0' and n == '0':
        break

    result = ''.join([c for c in n if c != d])
    result = result.lstrip('0')

    if result == '':
        print('0')
    else:
        print(result)
