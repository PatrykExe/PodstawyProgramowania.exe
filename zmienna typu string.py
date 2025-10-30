napis = 'kuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuurkuma'
#I: Fragment tekstu:
#1) Wycinanie od ... do\
print(napis[34:39]) # czyli tak naprawdę od 2 do 4

#2) Wycinanie od .. do (co ileś)
print(napis[0:40:2])

#3) wycinanie od początku
print(napis[:1])

#4) wycinanie do końca
print(napis[2:])

#5) czytanie od końca
print(napis[::])
print(napis[:])
print(napis[::-1])

#II: Zawieranie się znaku w słowie
#1)
if 'a' in napis:
    print("należy")
else:
    print("nienależy")

#III: Łączenie napisów (konkatenacja)
napis2 = napis + 'jestnajlepsza'
print(napis2)

#IV: Funkcje zmiennych typu string

#1) poszukiwanie danego fragmentu w tekście
napis3 = 'RaBaRbAr'
index_gdzie_jest = napis3.find('BaR')
print(index_gdzie_jest)

napis4 = 'alabalalalabala'
index_gdzie_jest2 = napis4.find('bala')
print(index_gdzie_jest2)

index_gdzie_jest3 = napis4.find('bala', index_gdzie_jest2 + 1)
index_gdzie_jest4 = napis4.find('ngd', index_gdzie_jest2 + 1)
print(index_gdzie_jest2)
print(index_gdzie_jest3)
print(index_gdzie_jest4)

if napis4.find('xyz') != -1:
    print('xyz jest w napisie')
else:
    print('nima')

#2) Podział tekstu na fragmenty
"""piec_liczb = input('Podaj pięć liczb. Odziel je przecinkiem')
piec_liczb_po_przedziale = piec_liczb.split(',')
print(piec_liczb_po_przedziale)
trzecia_liczba = int(piec_liczb_po_przedziale[2])
print(trzecia_liczba + 33)"""

#3) Łączenie napisów

lista_napisów = ['Windows', 'XP', 'został', 'stworzony', 'z', 'pasją']
cale_zdanie = ' '.join(lista_napisów)
print(cale_zdanie)

lista_napisow2 = ['Windows', 'XP', 'został', 'stworzony', 'z', 'pasją']
cale_zdanie2 = '\n'.join(lista_napisow2)
print(cale_zdanie2)

#3) zliczanie danego znaku w tekscie

napis5 = 'prawdopodobieństwo'
ile_razy_o = napis5.count('o')
print(ile_razy_o)