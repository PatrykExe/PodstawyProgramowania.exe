#                   Zadanie 5
lista = ['informatyka', 'matematyka', 'fizyka', 'geografia', 'biologia', 'chemia']

#1:
if "biologia" in lista:
    print("jest")
else:
    print("nima")

#2:
for x in lista:
    if x == "biologia":
        print("jest")
    else:
        continue
#3:

#4:
while True:
    if "biologia" in lista:
        print("jest")
        break
    else:
        continue