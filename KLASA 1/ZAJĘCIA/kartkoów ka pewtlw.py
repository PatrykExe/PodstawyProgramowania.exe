n = int(input("Podaj liczbę: "))

iloczyn = 1

for x in range(n):
    iloczyn = iloczyn * (x + 1)

print(iloczyn)



lista = [4, 12, 8, 1, 5, 6, 3]
licznik = 0

for x in range(len(lista)):
    for y in range(len(lista)):
        if lista[x] != lista [y] and (lista[x] + lista[y]) % 3 == 0:
            #print(lista[x], lista[y])
            licznik += 1
print(licznik)

for x in lista:
    for y in lista:
        if x != y and (x + y) % 3 == 0:
            #print(lista[x], lista[y])
            licznik += 1
print(licznik)




