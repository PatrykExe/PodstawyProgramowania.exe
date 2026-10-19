#1
zakres = 100
SITO = [True] * (zakres + 1)
SITO[0] = False
SITO[1] = False

for i in range(2, len(SITO)):
    if SITO[i]:
        for j in range(i * 2, len(SITO), i):
            SITO[j] = False

#Jak sprawdzć, czy 20 jest liczbą pierwszą?
print(SITO[20])




#2
def SITO(n):
    T = [1] * (n + 1)
    T[0] = 0
    T[1] = 0
    for i in range(2, n + 1):
        if T[i] == 1:
            for j in range(i * 2, n + 1, i):
                T[j] = 0
    return T
