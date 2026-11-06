dodawanie = lambda x, y: x + y
print(dodawanie(66, 1))


lista = ['abbg', 'nggaa', 'nygaaa']
lista.sort(key = lambda x: x.count('a'))
print(lista)


lista = [6, -9, 3, 0, -12, -1, 7]

#1)
lista.sort(key = lambda x: abs(x)) #abs = wartość bezwzględna

#2) sortowanie po długościach napisów
lista2 = ['matematyka', 'filozofia', 'fizyka', 'informatyka']
lista2.sort(key = lambda x: len(x)) # - przed len() sortuje od największej do najmniejeszej
print(lista2)

#3)sortowanie wielopoziomowe
ludzie = [['Janusz', 'Korwin'], ['Bartłomiej', 'Brzęczyszczykiewicz'], ['Janusz', 'Brzęczyszczykiewicz'], ['Bartłomiej', 'Korwin']]
ludzie.sort(key = lambda x: (x[0], x[1]))
print(ludzie)

#4) sortowanie po liczbie dzielników
def ile_dziel(liczba):
    ile = 0
    for d in range(1, liczba + 1):
        if liczba % d == 0:
            ile +=1
    return ile
print(ile_dziel(12))

lista3 = [12, 7, 1024, 9, 2137, 16]
lista3.sort(key = lambda x: ile_dziel(x))
print(lista3)

#II. Zaawansowane użycie funkcji map

lista4 = [1, 5, -6, 10, -7]
kwadraty = sorted(list(map(lambda x: x ** 2, lista4)))
print(kwadraty)

#zaawansowane mapowanie

slownik = {'fiz': 'fizyka', 'mat': 'matematyka', 'inf': 'informatyka'}
lista5 = ['fiz', 'jest', 'najlepsza', 'ale', 'inf', 'też', 'jednak', 'nic', 'nie', 'zastąpi', 'mat']

lista6 = list(map(lambda x: slownik[x] if x in slownik else x, lista5))
print(lista6)

