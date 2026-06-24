#Pętla zagnieżdżona w postaci tabliczki mnożenie do 100

for x in range(1, 11):
    line = str(x)
    for y in range(1, 11):
        #line += str(x), 3%e % str(y)
        print(f'{x} * {y} = {x * y}')
    if x <= 9:
        print(f'____{x+1}____')

print('___________________________________________')
for x in range(1, 21):
    for y in range(1, 21):
        print(x * y, end = '\t')
    print()

#trójkąt prostokątny
n = int(input('Wysokość trójkąta = '))
for d in range(n):
    for z in range(d+1):
        print('*', end = '')
    print()
df = chr(21328)
print(df)

for d in range(n):
    print('*' * (d + 1))

#trójkąt równoramienny
LSpace = n - 1
LGwiazd = 1

for i in range(n):
    print(' ' * LSpace, end = '')
    print('*' * LGwiazd)
    LSpace -=  1
    LGwiazd += 2