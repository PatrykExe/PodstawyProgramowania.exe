T = [-1, 3, 5, 7, 8, 9, 13, 33, 37, 40, 43]
n = len(T) - 1
x = 7
ile_p = 0
ile_k = 0
ile_w = 0

def F(T, x):
    global ile_p, ile_k
    p = 1
    k = n
    while p < k:
        s = (p + k) // 2
        if T[s] == x:
            return True
        else:
            if T[s] < x:
                ile_p += 1
                p = s + 1
            else:
                ile_k += 1
                k = s - 1
    return False

#ZAD. 2.1

F(T, x)
print(ile_p, ile_k)

#ZAD. 2.2
T = [x for x in range(1, 101)]
x = 101
n = len(T) - 1

ile_w = 0

F(T, x)

#ZAD. 3

n = 10
P = [0] * (n + 1)
S = [0] * (n + 1)

for i in range(1, n + 1):
    P[i] = 1
    S[i] = 0
for j in range(2, n + 1):
    if P[j] == 1:
        i = j * j
        while i <= n:
            P[i] = 0
            i = i + j
    S[j] = S[j - 1] + P[j]

print(P[1:])
print(S[1:])