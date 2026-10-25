#                           Zadanie 1)
t = 0
chwila = 1
while t <= 10:
    xt = 2 * t - 6
    yt = 4 * t - 5 * t ** 2
    if (chwila - 1) % 200 == 0:
        print(xt, ' ', yt)
    t += 0.01
    chwila += 1

#                           Zadanie 2)
file = open('ruch.txt')
dane = file.readlines()

for x in range(len(dane)):
    dane[x] = dane[x].split()

for i in range(len(dane)):
    dane[i][0] = int(dane[i][0])
    dane[i][1] = int(dane[i][1])
    def sz_sr(sc, tc):
        Vsr = sc / tc
        return Vsr
    print(sz_sr(dane[i][0], dane[i][1]))

#                           Zadanie 3)
x = 0
y = 0
t = 0

max_y = 0

while y >= 0:
    x = 15 * t
    y = 30 * t - 5 * t ** 2
    if y > max_y:
        max_y = y
    t += 0.01

print(f'a) {max_y}\nb) {x}\nc) {t}')
#                           Zadanie 4)

file2 = open('sily.txt')
dane2 = file2.readlines()

Fmax = 0

for x in range(len(dane2)):
    dane2[x] = dane2[x].split()
for i in range(len(dane2)):
    dane2[i][0] = float(dane2[i][0])
    dane2[i][1] = float(dane2[i][1])
    def sila(Fx, Fy):
        F = (Fx ** 2 + Fy ** 2) ** 0.5
        return F

    if sila > Fmax:
        Fmax = sila

print(Fmax)




