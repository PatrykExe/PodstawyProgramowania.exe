#Zadanie 1.2. ----------------------------------
def cosnapewno1(n):
    b = 1
    c = 0
    while n > 0:
        a = n % 10
        n = n // 10
        if (a % 2 == 0):
            c = c + b * (a // 2)
        else:
            c = c + b
        b = b * 10
    return c
print(cosnapewno1(87654321012345678))
#n = 33668 => c = 11314
#n = 542102 => c = 121101
#n = 87654321012345678 => c = 41312111011121314

#Zadanie 1.4. ----------------------------------

n = 10
T = 'tropikalny'
k = 5
S = [''] * (n + 1)

a = n // k
c = n - a
for i in range(1, n + 1):
    if i % k == 0:
        b = i // k
        S[n - a + b] = T[i - 1]
    else:
        S[c] = T[i - 1]
        c -= 1
print(''.join(S))

#defragmentacja => ajatemaredfgnc
#tropikalny => nlakportiy

#Zadanie 1.5. ----------------------------------
