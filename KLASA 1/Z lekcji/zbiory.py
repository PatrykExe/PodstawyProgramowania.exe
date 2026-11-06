zbior = {5, 6, 7 ,5, 2, 6, 6, 7}
print(zbior)

zbior2 = {'kot', 'windows', 'szlifierka', 'konstantynopoliczykowianeczka', 'kot'}
print(len(zbior2))

A = set(range(0, 20, 2))

B = {1, 2, 3, 4, 6, 12}

#suma zbiorów
AuB = A.union(B)
print(AuB)
AuB2 = set(list(A) + list(B))
print(AuB2)

#Część wspólna
AnB = A.intersection(B)
print(AnB)

#Różnica
A_B = A.difference(B)
print(A_B)

#Dodawanie elementów do zbioru
C = {1, 7, 5, 4}
C.add(10)
print(C)

