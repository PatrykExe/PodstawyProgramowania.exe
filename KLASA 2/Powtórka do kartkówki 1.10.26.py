#Zadanie 2
n = 3
s = 1
p = 1
for k in range(1, n + 1):
    s = s + p
    for i in range(1, k + 1):
        p = p * k
        print(k, i, s, p)

#Zadanie 3
#Zadanie 2

T = [-1, 27, 6, 13, 4, -3, -2, -3]
n = len(T) - 1
x = 30

def d(x):
    global n
    n = n + 1
    T.append(x)