#2.1
plik = open('liczby.txt')
dane = plik.readlines()

for x in range(len(dane)):
    dane[x] = dane[x].strip()

for y in dane:
    if int(y[::-1]) % 17 == 0:
        print(y[::-1])
print('--------------------')
#2.2
print(len(set(dane)))

liczby = set()

for x in dane:
    if dane.count(x) == 2:
        liczby.add(x)
    else:
        continue
print(len(liczby))
print('--------------------')
licznik = 0
for i in set(dane):
    if dane.count(i) == 3:
        licznik += 1
print(licznik)


#3
plik = open('ruch.txt')
dane = plik.readlines()

for x in range(len(dane)):
    dane[x] = dane[x].split()
    dane[x] = list(map(float, dane[x]))

def t(i):
    return (i-1) / 100

def V_sr(rk, rp, dt):
    return [(rk[0] - rp[0]) / dt, (rk[1] - rp[1]) / dt]

def sz_sr(v_sr):
    return (v_sr[0] ** 2 + v_sr[1] ** 2) ** 0.5

wynik = []
for i in range(1, len(dane)):
    rp = dane[0]
    rk = dane[i]
    czas = t(i + 1)
    pr_sr = V_sr(rk, rp, czas)
    szybkosc_sr = sz_sr(pr_sr)
    wynik.append((czas, szybkosc_sr))

print(wynik)