#symbole logiczne

#koniunkcja
print(2 == 3 and 3 > 1)

#Alternatywa
login = 'Pk'
haslo = 'KP'
print(login == 'pK' or haslo == 'KP')

#zaprzeczenie
print(not(login == 'Pk' or haslo == 'kP'))

#Alternatywa Wykluczająca
fryzjer = True
murarz = False

print(fryzjer == True ^ murarz == True)

#Priorytety operatorów logicznych
print(2 == 3 and 3 < 1 or 2 < 6)

#operatory standardowe
print(2 + 4)
print(2 - 4)
print(2 * 4)
print(2 / 4)

#Potęgowanie
print(2 ** 4)

# Pierwiastki
print(36 ** 0.5)
print(125 ** (1/3))

#dzielernie całkowite (div) - zaokrąglenie zawsze w dół do liczby całkowitej
print(22 // 5)

#reszta z dzielenia
print(12 % 5)