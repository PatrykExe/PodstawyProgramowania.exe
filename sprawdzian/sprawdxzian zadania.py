#Zadanie 1.1

file = open('prostokaty.txt')
dane = file.readlines()
boki = []
for w in dane:
    para = w.split()
    prostokat = (int(para[0]), int(para[1]))
    boki.append(prostokat)
print(boki)


boki.sort(key = lambda x: x[0] * x[1])
p_min = boki[0]
p_max = boki[-1]

print(p_min[0] * p_min[-1], p_max[0] * p_max[-1])


#Zadanie 1.2
obwody = []

for p in boki:
    obwod = 2 * p[0] + 2 * p[1]
    obwody.append(obwod)

obwody = set(obwody)
print(len(obwody))