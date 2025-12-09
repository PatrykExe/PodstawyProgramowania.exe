# #Pętla while - przykłady
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
        print('Nima hasla - nima wstepu')