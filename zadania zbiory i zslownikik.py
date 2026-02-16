lista2d = [
[5, 2, 8, 5, 1],
[3, 8, 2, 9, 5],
[1, 4, 4, 2, 7],
[6, 3, 9, 1, 4],
[8, 2, 5, 6, 3]
]
zbior = set()
zbior2 = {}
zbior_caly = set()
for x in range(len(lista2d)):
    for y in range(len(lista2d[0])):
        element = lista2d[x][y]
        zbior.add(element)
print(zbior)

for x in lista2d:
    zbior2 = set(x)
    zbior_caly = zbior_caly.union(zbior2)
print(zbior_caly)

lista1d = []
for x in range(len(lista2d)):
    for y in range(len(lista2d[0])):
        element = lista2d[x][y]
        lista1d.append(element)


slowa = [
    "LETTER",
    "BALLOON",
    "SUCCESS",
    "HAPPY",
    "COFFEE",
    "BOOKKEEPER",
    "ASSESS",
    "MISSISSIPPI",
    "ADDRESS",
    "TOOLBOX"
]

max_x = ''
max_l_r_l = 0
for x in slowa:
    y = set(x)
    l_r_l = len(y)
    if l_r_l > max_l_r_l:
        max_l_r_l = l_r_l
        max_x = x
    #print(f'{x} {len(y)}')
print(max_x)

#sposób 2
max_slowo = max(slowa, key = lambda x: len(set(x)))
print(max_slowo)

#2.2
zbior = set()
for x in slowa:
    for y in x:
        zbior.add(y)
print(zbior)

for l in sorted(zbior):
    lista = []
    for s in slowa:
        if l in s:
            lista.append(s)
    print(f'{l}: {lista}')
