# import random
# #                           ZADANIE 2.4
# In = int(input("Podaj liczbę Rzeczywistą: "))
# Out = int(input("Podaj liczbę Rzeczywistą: "))
# def losuj_z_przedzialu():
#     print(random.randint(In, Out))
#
# losuj_z_przedzialu()
#
# #                           ZADANIE 2.5
#
# slownik = {'Data': '966 rok naszej ery',
#            'Nazwa': 'Chrzest Polski',
#            'Opis': 'Mieszko I przyjmuje chrzest, czym zapewnia'
#                    ' Polsce bezpieczniejszą pozycję w ówczesnej'
#                    ' Europie.'
# }
# def notatka():
#     print(f'{slownik['Nazwa']} odbył się w {slownik['Data']}. Krótko mówiąc: {slownik['Opis']}')
#
# notatka()

#                           ZADANIE 2.6
def unikatowe_elementy(arg1, arg2):
    arg = arg1 + arg2
    elementy = set()
    for x in arg:
        if arg.count(x) == 1:
            elementy.add(x)
    return elementy
print(sorted(unikatowe_elementy([1, 2, 6, 4, 5], [8, 4, 5, 2])))

def unikatowe_elementy2(l1, l2):
    zbior = set()
    l = l1 + l2
    for x in l:
        if x in l1 and x in l2:
            pass
        else:
            zbior.add(x)
    return zbior

#                           ZADANIE 2.7
# liczba = int(input('Podaj liczbę całkowitą +'))
# def suma_dzielników():
#     suma_dzielniki = 0
#     for x in range(1, liczba + 1):
#         if liczba % x == 0:
#             suma_dzielniki += x
#     print(suma_dzielniki)
# suma_dzielników()
#
# #                           ZADANIE 2.8
#
# def liczba_liczb(liczba):
#     licznik = 0
#     while liczba > 0:
#         liczba = liczba // 10
#         licznik += 1
#
#     return licznik
# print(liczba_liczb(1828332))

