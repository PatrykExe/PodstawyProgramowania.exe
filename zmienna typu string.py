napis = 'kuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuurkuma'
#I: Fragment tekstu:
#1) Wycinanie od ... do\
print(napis[34:39]) # czyli tak naprawdę od 2 do 4

#2) Wycinanie od .. do (co ileś)
print(napis[0:40:2])

#3) wycinanie od początku
print(napis[:1])

#4) wycinanie do końca
print(napis[2:])

#5) czytanie od końca
print(napis[::])
print(napis[:])
print(napis[::-1])

#II: Zawieranie się znaku w słowie
#1)
if 'a' in napis:
    print("należy")
else:
    print("nienależy")