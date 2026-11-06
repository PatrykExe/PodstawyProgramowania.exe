#Palindromy
slowo_podstawowe = input('Podaj dowolne słowo (nie używaj znaków charakterystycznych dla różnych języków): ')
odwrocone_slowo = slowo_podstawowe[::-1]

if slowo_podstawowe == odwrocone_slowo:
    print('Podane słowo jest palindromem')
else:
    print('Nah, to nie jest palindrom')

#Zadanie 2 z próbnej kartkóweczki ;)
slowo = 'BRNQZPFXLMWUGTSHPDAAOVKICNRTEQYBPMZEFDCXHJMFAOTLPMXGSAQWETRMADYUBXCNPLKJYHOFA'
haslo = slowo[9::10]
print(haslo)

#Zadanie 3 z próbnej kartkóweczki ;)
slowo = 'częstochowa'
# 1. operator in
if 'stoch' in slowo:
    print('A no rzeczywiście jest')
else:
    print('Nah, nima')

# 2. funkcja find()

CzyJest = slowo.find('stoch')
if CzyJest != -1:
    print('A no rzeczywiście jest')
else:
    print('Nah, nima')

#3. funkcja count()
CzyJest2 = slowo.count('stoch')
if CzyJest2 != -1:
    print('A no rzeczywiście jest')
else:
    print('Nah, nima')

#Zadanie 4 z próbnej kartkóweczki ;)
slowo2 = input("Podaj słowo zawierające tylko litery a, b, c i d: ")

litery = {'a': 0, 'b': 0, 'c': 0, 'd': 0}

for znak in slowo:
    if znak in litery:
        litery[znak] += 1

print("W podanym słowie znajdują się litery a, b, c i d w następujących ilościach:")
for litera in ['a', 'b', 'c', 'd']:
    print(f"Litera {litera}: {litery[litera]}")

#Zadanie 5 z próbnej kartkóweczki ;)
a, b, c = map(float, input("Podaj trzy liczby rzeczywiste: ").split())
# map() służy do zastosowania jakiejś funkcji do każdego elementu, bez rozpisywania skryptu na kilka linijek
suma = a + b + c

print("Suma podanych liczb to:", suma)
