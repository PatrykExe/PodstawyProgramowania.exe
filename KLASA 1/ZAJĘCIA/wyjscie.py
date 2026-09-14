#1. Co można wyświetlać print'em
print(5)
print((2 + 2) * 2)

x = 34
print(x)

print("nigga")
print(round(2.137, 2))
print(2 == 3 and 1 > 0)
print([6, 1, 9, 4, 2])

#2. Formatowanie wyświetlania tekstu

imie = input("Podaj swoje Imie: ")
nazwisko = input("Podaj swoje Nazwisko: ")
wiek = int(input("Podaj swój wiek: "))

#Sposób 1

print("Witaj " + imie + ' ' + nazwisko + ". Masz "+ str(wiek) + " lat. Za 5 lat będziesz mieć " + str(wiek + 5) + " lat")

#Sposób 2

print("Witaj", imie, nazwisko, ". Masz", wiek, "lat. Za 5 lat będziesz mieć", wiek + 5, "lat.")

#Sposób 3

print(f'Witaj {imie} {nazwisko}. Masz {wiek} lat. Za 5 lat będziesz mieć {wiek + 5} lat')

#Sposób 4.1

print('Witaj {} {}. Masz {} lat. Za 5 lat będziesz mieć {} lat.'.format(imie, nazwisko, wiek, wiek + 5))

#Sposób 4.2

print('Witaj {1} {0}. Masz {4} lat. Za 5 lat będziesz mieć {3} lat.'.format(nazwisko, imie, wiek + 5, wiek))