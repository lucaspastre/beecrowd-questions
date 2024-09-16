import math

n = int(input())
for i in range(n):
    total = 0
    casas = int(input())
    for j in range(0, casas):
        total += 2**j

    gramas = total / 12
    kg = gramas / 1000
    kg = math.floor(kg)

    print(f'{kg} kg')
