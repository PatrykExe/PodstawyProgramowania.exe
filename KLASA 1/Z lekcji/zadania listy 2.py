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

#zadanie 4.

tekst = 'LITWOOJCZYZNOMOJATYJESTESZJAKZDROWIEILECIETRZEBACENICTENTYLKOSIEDOWIEKTOCIESTRACILDZISPIEKNOSCTWACALEJOZDOBIEWIDZEIOPISUJEBOTESKNIEPOTOBIEPANNOSWIETACOJASNEJBRONISZCZESTOCHOWYIOSTREJSWIECISZBRAMIETYCOGRODZAMKOWYNOWOGRODZKIOCHRANIASZZJEGOWIERNMLUDEMJAKMNIEDZIECKODOZDROWIAPOWROCILASCUDYMGDYODPLACZACEJMATKIPODTWOJAOPIEKEOFIAROWANYMARTWAPODNIOSELMOJEPOWIEKEIZARAZMOGLEMPIESZODOTWYCZSWIATYNPROGUISTZAWROCONEZYCIEPODZIEKOWACBOGUTAKNASPOWROCISCUDYMNADOJCZYZNYLONOTYMCZASEMPRENOSMOJADUSZEUTESKNIONADOTYCHPAGORKOWLESNYCHDOTYCHLAKZIELONYCHSZEROKONADBLEKITNYMNIEMNEMROZCIAGNIONYCHDOTYCHPOLMALOWANYCHZBOZEMROZMAITEMWYZLACANYCHPSZENICAPOSREBRZANYCHZYTEMGDZIEBURSZTYNOWYSWIERZOPGRYKAJAKSNIEGBIALAGDZIEPANIENSKIMRUMIENCEMDZIECIELINAPALAAWSZYSTKOPRZEPASANEJAKBYWSTEGAMIEDZAZIELONANANIJZZADKACICHEGRUSZESIEDZA'
#Sposób 1
tekstZmiana = 0
for x in tekst:
    tekstZmiana += ord(x)
print(tekstZmiana)

#Sposób 2

print(sum(map(ord, tekst)))
# zadanie 6

plansza = [
[3, 8, 1, 9]
[4, 6, 5, 2]
[7, 1, 8, 3]
[2, 9, 4, 6]
]

# Zadanie 6.1.
'''
#średnie w wierszach
for x in plansza:
    print(sum(x) / len(x))

#średnie w kolumnach
for i in range(len(plansza[0])):
    suma = 0
    for j in range(len(plansza)):
        suma += plansza[j][i]
    print(suma / len(plansza))'''

# Zadanie 6.2.

for i in range(len(plansza)):
    for j in range(len(plansza[0])):
        licznik = 0
        srodkowy = plansza[i][j]  # szary element
        '''if srodkowy < plansza[i - 1][j]:
            licznik += 1
        if srodkowy < plansza[i + 1][j + 1]:
            licznik += 1'''

        for x in range(i - 1, (i + 1) + 1):
            for y in range(j - 1, (j + 1) + 1):
                if i < 0:
                    x = len(plansza) - 1
                elif x > len(plansza) - 1:
                    x = 0
                if y < 0:
                    y = len(plansza[0]) - 1
                elif y > len(plansza[0]) - 1:
                    y = 0
                czerwony = plansza[x][y]
                if srodkowy < czerwony:
                    licznik += 1
        print(i, j, licznik)






































