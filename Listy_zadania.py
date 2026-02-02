#Zadanie 1/

lista1 = [12, -9, 6, 2, 8, 1, 15, -7, 0, 1, 1, 2, 2, -7, 2, 1, -7, 2]
lista2 = [['pies', 'wilk'], ['kot domowy', 'tygrys', 'lew'], 'kapibara', 'mrówka', ['rekin', 'śledź', 'pstrąg']]

#a)
print(lista2[1][2])

#b)
print(list(lista2[3]))

#c)
lista3 = lista1[2::2]
print(lista3)

#d)
lista2.append(lista2[1] * 3)
print(lista2)

#e)
lista1 = lista1 + [9, 6, 16, -8, 7]
print(lista1)

#f.1)
#lista1.sort()
uw = sorted(lista1)
print(uw[0], uw[-1])
print(min(lista1), max(lista1))

#g)
# del lista1[4]
# print(lista1)

#h)
del lista1[4:9]
print(lista1)

#i)

#j)
'''lista3 = [x ** 2for x in lista1]'''

lista3 = []
for x in lista1:
    lista3.append(x ** 2)
print(lista3)

#2
