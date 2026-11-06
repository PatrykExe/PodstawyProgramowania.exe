# plik = open('dane.txt')
# dane = plik.read()
# print(dane)

plik2 = open('dane2.txt')
dane2 = plik2.readlines()

for i in range(len(dane2)):
    dane2[i] = int(dane2[i])
print(dane2)

plik3 = open('dane3.txt')
dane3 = plik3.readlines()
print(dane3)

for i in range(len(dane3)):
    dane3[i] = dane3[i].strip()
print(dane3)

plik4 = open('dane_IV.txt')
dane_IV = plik4.readlines()

for i in range(len(dane_IV)):
    dane_IV[i] = dane_IV[i].split()
print(dane_IV)

plik5 = open('daneV.txt')
daneV = plik5.readlines()

for i in range(len(daneV)):
    daneV[i] = daneV[i].split()
    for j in range(len(daneV[i])):
        daneV[i][j] = int(daneV[i][j])

print(daneV)

daneVx = [list(map(int, w.split())) for w in open('dane5.txt')]