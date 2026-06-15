t = 0
chwila = 1
while t <= 10:
    x = 2 * t - 6
    y = 4 * t - 5 * t ** 2
    if (chwila - 1) % 200 == 0:
         print(x, y)
    t += 0.01
    chwila += 1


plik = open('sprawdzian/sily.txt')
dane = plik.readlines()

for i in range(len(dane)):
    dane[i] = dane[i].split()
    dane[i][0] = float(dane[i][0])
    dane[i][1] = float(dane[i][1])

max_sila = 0
max_F = []
for F in dane:
    sila = (F[0] ** 2 + F[1] ** 2) ** 0.5
    if sila > max_sila:
        max_sila = sila
        max_F = F

print(max_F, F)