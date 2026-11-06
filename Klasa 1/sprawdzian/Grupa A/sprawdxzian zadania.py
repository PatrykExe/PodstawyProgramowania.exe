#GRUPA A

# #Zadanie 1.1
#
# file = open('prostokaty.txt')
# dane = file.readlines()
# boki = []
# for w in dane:
#     para = w.split()
#     prostokat = (int(para[0]), int(para[1]))
#     boki.append(prostokat)
# print(boki)
#
#
# boki.sort(key = lambda x: x[0] * x[1])
# p_min = boki[0]
# p_max = boki[-1]
#
# print(p_min[0] * p_min[-1], p_max[0] * p_max[-1])
#
#
# #Zadanie 1.2
# obwody = []
#
# for p in boki:
#     obwod = 2 * p[0] + 2 * p[1]
#     obwody.append(obwod)
#
# obwody = set(obwody)
# print(len(obwody))
#
# #Zadanie 2
# print('ZADANIE 2')
#
# plik = open('slowa.txt')
# dane = plik.readlines()
# #Zadanie 2.1
# licznik = 0
#
# for l in dane:
#     l = l.strip()
#     for i in range(len(l) - 2): #Aby dobrze policzyło
#         if l[i - 1] == 'k' and l[i + 1] == 't':
#             licznik += 1
#
# print(licznik)
# #Zadanie 2.2
# plik = open('liczby.txt')
# dane = plik.readlines()
#
# for linia in dane:
#     linia = linia.strip()
#     srodek = linia[len(linia) // 2]
#     ile_srodek = linia.count(srodek)
#     max_ile = 0
#     for znak in linia:
#         ile = linia.count(znak)
#         if ile > max_ile:
#             max_ile = ile
#     if ile_srodek == max_ile:
#         print(linia)
#
#
# #Zadanie 3
# print('ZADANIE 3')
#
# liczby = 0
# licznik = []
# file3 = open('liczby.txt')
# dane3 = file3.readlines()
#
# for x in dane3:
#     x = x.strip()
#     if x[0] == x[-1]:
#         liczby += 1
#         licznik.append(x)
#
# print(liczby, licznik[1])

#GRUPA B

