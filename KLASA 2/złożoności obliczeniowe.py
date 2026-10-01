#Przykład 1
n = 5

for i in range(n):
    for j in range(n):
        print(i + j)

#Przykład 2
l = 5

for i in range(3):
    for j in range(l):
        print(i * j)

#Przykład 3
suma = 0
liczba = 127

while liczba > 0:
    suma += liczba % 10
    liczba //= 10
print(suma)

#Zadanie 1
