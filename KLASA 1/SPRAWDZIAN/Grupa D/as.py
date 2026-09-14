#1.2
plik = open('dane.txt')
dane = plik.read().strip()

listaLiczb = []
for i in range(1, len(dane) - 1):
    if dane[i].isdigit() and not dane[i - 1].isdigit():
        start = i
    elif dane[i].isdigit() and not dane[i + 1].isdigit():
        stop = i
        listaLiczb.append(int(dane[start:stop + 1]))
print(max(listaLiczb) ** 2)

#3.1 i 3.3
def f(x):
    return 2 * (x + 3) * (x - 2) * (x - 6) * (x - 7)
print(f(5))

przedzial = [-3, -2.99, -2.98, -2.97]

def CzyRosnacaWPrzedziale(przedzial):
    for i in range(1, len(przedzial)):
        x2 = przedzial[i]
        x1 = przedzial[i - 1]
        if f(x2) <= f(x1):
            return False
    return True