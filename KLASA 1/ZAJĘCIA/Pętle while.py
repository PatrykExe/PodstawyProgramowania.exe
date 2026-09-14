"""# #Pętla while - przykłady
#
# liczba = 120
# licznik = 0
#
# # W pętli while podajemy warunek trwania pętli
# while liczba > 0:
#     liczba = liczba // 2
#     licznik = licznik + 1
#
# print(licznik)
#
# #Zadanie 1:
# LBWK = input('Podaj liczbę, lub q aby zakończyć:')
# licznik2 = 0
# while LBWK != 'q':
#     liczba = int(LBWK)
#     if liczba < 2:
#         licznik2 = licznik2 + 1
#     LBWK = input('Podaj liczbę, lub q aby zakończyć:')
# print(licznik2)

#Zadanie 2
popr_haslo = "Luksemburk"
haslo = input("Podaj haslo: ")
proba = 1

while haslo != popr_haslo and proba < 5:
    print("Hasło błędne, podaj jeszcze raz: ")
    haslo = input("Podaj haslo ponownie: ")
    proba = proba + 1
    if haslo == popr_haslo:
        print('Welcome')
    else:
        print('Nima hasla - nima wstepu')"""
"""import time
from random import randint
x = 0
punkty1 = 0
punkty2 = 0

while not ((punkty1 >= 21 or punkty2 >= 21) and abs(punkty1 - punkty2 >= 2)):  #abs(x) = |x|
    x += 1
    print(f'Wynik: {punkty1} : {punkty2}')
    print(f'Akcja {x}:')
    #runda = int(input("Podaj która drużyna wygrała (1/2): "))
    runda = randint(1,2)
    if runda == 1:
        punkty1 += 1
    elif runda == 2:
        punkty2 += 1
    time.sleep(10)

if punkty1 > punkty2:
    print("Wygrała drużyna 1")

elif punkty1 < punkty2:
    print('Wygrała drużyna ')
"""

liczba = int(input('Podaj liczbę: '))

while liczba > 0:
    cyfra = liczba % 10
    liczba = liczba // 10
    print(cyfra, end = '')
# 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67


liczba2 = int(input('Podja liczbe: '))
d = 2
ile_czyn = 0
ile_r_czyn = 0
while liczba2 > 1:
    if liczba2 % d == 0:
        ile_r_czyn += 1
    while liczba2 % d == 0:
        liczba2 = liczba2 // d
        ile_czyn += 1
    d += 1
print(ile_czyn)
print(ile_r_czyn)




























