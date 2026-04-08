#Zadanie 1.1
file = open('bin_przyklad.txt')
dane = file.readlines()
for x in dane:
    x = x.strip()
    def bloki(bin):
        count = 1
        poprzednie_a = bin[0]
        for a in bin[1:]:
            if a != poprzednie_a:
                count += 1
                poprzednie_a = a
        return count
print(bloki(x))