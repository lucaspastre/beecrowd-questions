n = int(input())
for a in range(0, n):
    palavra = input()[::-1]
    palavra = list(palavra)
    for i in range(0, len(palavra)):
        if palavra[i].islower():
            print(palavra[i], end='')
    print()
