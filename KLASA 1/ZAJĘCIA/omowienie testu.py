from math import inf # niskuńczunuść
'''lista = [12, 45, 78, 101, -5, 9, 0]

# zadanie 2
# Sposob 1
for i in range(len(lista)):
    if i % 2 != 0:
        print(lista[i])

# Sposób 2
for i in range(1, len(lista), 2):
    print(lista[i])

# Sposób 3
for i in lista[1::2]:
    print(i)'''

lista3 = [1]
for a in lista3:
    lista3.append(1)
    b = int(input("Podaj lićbe "))
    print(b)
    if b == 0:
        break
    else:
        continue

#Zadanie 17
n = int(input("Podaj, ile będzie liczb"))
suma = 0
max_liczba = -inf
min_liczba = inf
ile_mniej_3 = 0
ile_przedzial = 0

for x in range(n):
    liczba = int(input("Podaj liczbę: "))
    suma += liczba
    if liczba > max_liczba:
        max_liczba = liczba
    if liczba > min_liczba:
        min_liczba = liczba
    if liczba < 3:
        ile_mniej_3 += 1
    if liczba > -2 and liczba <= 11:
        ile_przedzial += 1

print(suma)
print(suma / n)
print(max_liczba)
print(min_liczba)
print(ile_mniej_3)
print(ile_przedzial)


lista67 = []
for x in range(n):
    liczba = int(input('podaj liczbe'))
    lista67.append(liczba)
print(sum(lista67))
print(sum(lista67) / n)
print(max(lista67) / n)
print(min(lista67) / n)

