#Zadania 2.
lista = [178, 192, 184, 182, 180, 179, 186, 190, 191, 191]

x_max = max(lista)
x_min = min(lista)

lista_norm = [(x - x_min) / (x_max - x_min) for x in lista]
print(lista_norm)

#zadanie 3.
lista2 = [123, 89, 5600, 432, 11, 45, 900, 12450, 1410, 390, 9999]
'''lista2 = [x for x in lista2 if x < 1000 or x > 9999]'''
lista = [x for x in lista2 if not (x >= 1000 and x <= 9999)]





















































#---67---