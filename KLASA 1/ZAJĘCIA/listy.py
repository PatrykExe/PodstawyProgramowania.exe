#1) Listy a napisy
napis = 'informatyka'
lista = list(napis)
print(lista)
lista = '.'.join(lista)
print(lista)

#2) Zakres a lista
zakres = range(4,5,2)
lista2 = list(zakres)
print(lista2)

#3) Indeksowanie elementów listy
lista3 = ['osa', 99, 3.14, [5, 6, 3, 5]]
print(lista3[1:3])
print(lista3[3][2])
print(lista3[3][::2])

#4) Powielanie listy
#Dodawanie list
lista4 = ['a', 3, 66]
lista5 = ['f', 45, [8, 'tg']]
lista6 = lista5 + lista4
print(lista6)

#Dodawanie list 2
lista7 = ['a', 3, 66]
lista8 = ['f', 45, [8, 'tg']]
lista8.extend(lista7)
print(lista8)

# "mnożenie" listy przez liczbę
lista9 = [0] * 2137

print(lista9)

#5 Sortowanie i odwracanie listy
lista10 = [4 ,2, 5, 72, 41, 212, 67, 23]
#lista10.sort()
lista10.reverse()
print(lista10)

#6) wyrażenia listowe
lista11 = list(range(1, 11))
lista11_kwadraty = [x ** 2 for x in lista11 if x % 2 == 0]
print(lista11_kwadraty)

#7) usuwanie elementów
#7.1)usuwanie elementu na bazie jego wartości
lista12 = [4, 67, 8, 44, 67, 18]
#lista12.remove(67) #usuwa pierwszy element od lewej
while 67 in lista12:
    lista12.remove(67)
print(lista12)

#7.2 usuwanie elementu na bazie jego indexu
del lista12[1]
print(lista12)