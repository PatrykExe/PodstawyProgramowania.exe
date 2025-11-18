napis = 'kuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuurkuma'
#I: Fragment tekstu:
#1) Wycinanie od ... do\
print(napis[34:39]) # czyli tak naprawdę od 34 do 38

#2) Wycinanie od .. do (co ileś)
print(napis[0:40:2]) #(trzecia wartość - co 2 litera jest wyświetlana

#3) wycinanie od początku
print(napis[:1]) #Zostawienie pustego jest równoważne z 0

#4) wycinanie do końca
print(napis[2:]) #usuwa pierwsze 2 litery

#5) czytanie od końca
print(napis[::])
print(napis[:])
print(napis[::-1])

#II: Zawieranie się znaku w słowie
#1)
if 'a' in napis:
    print("należy")
else:
    print("nima")

#III: Łączenie napisów (konkatenacja)
napis2 = napis + 'jestnajlepsza' #podajesz zdefiniowane słowo i dodajesz to co chcesz dodać
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
#"!= -1" oznacza, że cośnie jest równe temu, że nie znaleziono, czyli poprostu znaleziono

#2) Podział tekstu na fragmenty

piec_liczb = input('Podaj pięć liczb. Odziel je przecinkiem')
piec_liczb_po_przedziale = piec_liczb.split(',')
print(piec_liczb_po_przedziale)
trzecia_liczba = int(piec_liczb_po_przedziale[2])
print(trzecia_liczba + 33)

#3) Łączenie napisów

lista_napisów = ['Windows', 'XP', 'został', 'stworzony', 'z', 'pasją']
cale_zdanie = ' '.join(lista_napisów) #join() umożliwia podanie 'separatora', którym będą oddzielone elementy listy
print(cale_zdanie)

lista_napisow2 = ['Windows', 'XP', 'został', 'stworzony', 'z', 'pasją']
cale_zdanie2 = '\n'.join(lista_napisow2) #\n odpowiada za przeniesienie kolejnych elementów do innych następnych linijek
print(cale_zdanie2)

#4) zliczanie danego znaku w tekscie

napis5 = 'prawdopodobieństwo'
ile_razy_o = napis5.count('o') #count() odpowiada za zliczenie elementów słowa lub listy, które zostały wybrane (np. a lub 12)
print(ile_razy_o)

#5 'Mutowalność' stringów
napis6 = 'fiwyka'
# napis6[2] = 'z'
# print(napis6)
#Nie da się 'podmieniać' pojedyńczych znaków w stringach

#Sposób na to coś
napis6_lista = list(napis6)
print(napis6_lista)
napis6_lista[2] = 'z'
print(napis6_lista)
napis6_gotowy = ''.join(napis6_lista)
print(napis6_gotowy)

#6) Długość napisu
napis7 = 'językpolski'
print(len(napis7))

#7) Powielanie stringa
napis8 = 'google maps'
print(napis8 * 3)

#-----------------------------------------------------------------------------------------------------------------------

# Funkcje testujące cyfry i litery
napis9 = 'kobalt20'
if napis9.isalpha() == True:
    print('Słowo składa się tylko z liter')
else:
    print('Słowo nie składa się tylko z liter')

napis10 = '1410'
if napis10.isdigit() == True:
    print('same cyfry')
else:
    print('nie same cyfry')

napis11 = '1410w'
if napis11.isalnum() == True:
    print('cyfry i litery')
else:
    print('nie cyfry i litery')