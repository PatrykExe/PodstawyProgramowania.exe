#Zadanie 15
X = list(range(0, 103, 3))

print('x\ty')
# for x in X:
#     y = 0.5 * x * 3
#     print(f'{x}\t{y}')

# for x in range(0, 103, 3):
#     y = 0.5 * x * 3
#     print(f'{x}\t{y}')
#b
for x in range(-30, 61):
    x = x / 10
    y = 0.5 * x + 3
    if x >= 0:
        print(f'{x}\t\t{y}')
    else:
        print(f'{x}\t{y}')

lista1 = list(range(3, 31, 3))
lista2 = list(range(11, 111, 11))
lista3 = list(range(13, 131, 13))

print(lista1, lista2, lista3)
#Sposób 1
for b, w, u in zip(lista1, lista2, lista3):
    print(f'{b}\t{w}\t{u}')

#Sposób 2
for i in range(10):
    print(f'{lista1[i]}\t{lista2[i]}\t{lista3[i]}')

lista10 = [21, 37, 67, 69]

for q in lista10:
    print(q)

for i in range(len(list(lista10))):
    print()
#17)
n = int(input('Podaj ile będzie liczb: '))

for x in range(n):
    liczba = int(input('Podaj liczbę: '))
