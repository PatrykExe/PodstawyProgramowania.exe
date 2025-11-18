# # # #Co to to nie, no panie, tak to nie
# # #
# # # a = float(input('Podaj liczbę: '))
# # # b = float(input('Podaj liczbę: '))
# # # c = float(input('Podaj liczbę: '))
# # # d = float(input('Podaj liczbę: '))
# # # e = float(input('Podaj liczbę: '))
# # # suma = f'{a+b+c+d+e}'
# #
# liczba = 0
# suma = 0
#
# for zx in range(5):
#     liczba = float(input('Podaj liczbę: '))
#     suma = suma + liczba
#
# print(suma)
#
# #1. listy
# lista = ['qwerty', 56, [6, 7], 21.37, [[5, 44], 1], 67]
# print(lista[2][1])
# print(lista[4][0][1])
#
# #2 Listy i pętle
# lista2 = ['kot', 'Szlifierka kątowa bosch', 'poziomica', 'ognisko']
#
# #Pętla for:
# #->wyciąga dane z listy (jedna po drugiej)
# #->wykonuje się tyle razy ile elementów ma lista
# for n in lista2:
#     print(n)
#
# #Pętla, która wykona się 3 razy
# lista3 = [15787, 845183, 67]
#
# for i in lista3:
#     print('OK')
#
# #Pętla, która wykonuje się 1000 razy
# lista4 = [0] * 1000
# for i in lista4:
#     print('cześć')
#
# #Pętla, która wykonuje się 10 razy
# lista4 = [0] * 10
# for i in lista4:
#     print('cześć')
#
# #3. Generatory i pętle
#
# przedzial = range(1, 10) #<1; 10)
# print(przedzial)
#
# for i in przedzial:
#     print(i)
#
# #Pętla 10x
# print(' ')
#
# for i in range(10): #range(0, 10)
#     print(i)

lista67 = [0]
lista67.append(0)
print(lista67)

# for i in lista:
#     print('cześć')
#     lista.append(0)

while True:
    print('x')