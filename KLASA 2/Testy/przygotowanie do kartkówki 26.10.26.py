#Algorytm euklidesa
    #Algorytm Euklidesa służy do szybkiego wyznaczania
    #Największego Wspólnego Dzielnika (NWD) dwóch liczb całkowitych.

def NWD(a, b):
  while b != 0:
    a, b = b, a % b
  return a

print(NWD(18, 48))

#Sito Eratostenesa
    #Sito Eratostenesa to efektywny algorytm służący do znajdowania
    # wszystkich liczb pierwszych w zadanym zakresie od 2 do n

def SITO(n):
    T = [1] * (n + 1)   #Lista samych "1" o długości n + 1
    T[0] = 0   #pierwsza liczba z definicji nie jest liczbą pierwszą
    T[1] = 0   #druga liczba z definicji nie jest liczbą pierwszą

    for i in range(2, n + 1):   #Pętla przechodząca przez wszystkie liczby aż do n + 1
        if T[i] == 1:   #Sprawdza czy dana liczba nie została wykluczona
            for j in range(i * 2, n + 1, i):   #Wyklucza wielokrotności liczby i, jeżeli jest liczbą pierwszą
                T[j] = 0
    return T
print(SITO(10))
