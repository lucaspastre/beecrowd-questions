def primo(numero):
    if numero < 2:
        return False
    for j in range(2, int(numero ** (1/2)) + 1):
        if numero % j == 0:
            return False
    return True

n = int(input())
for i in range(n):
    num = int(input())
    if primo(num):
        print('Prime')
    else:
        print('Not Prime')
