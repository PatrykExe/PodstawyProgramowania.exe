# algorytm łopatologiczny
def czy_pierwsza(n):
    dzielniki = 0
    # Zliczamy dzielniki liczby n
    for i in range(1, n + 1):
        if n % i == 0:
            dzielniki += 1
    #jeśli są dokładnie dwa dzielniki to liczba n jest pierwsza
    if dzielniki == 2:
        return True
    else:
        return False


def czy_pierwszav2(n):
    if n == 1:
        return False
    else:
        for d in range(2, int(n ** 0.5) + 1):
            if n % d == 0:
                return False
        return True
print(czy_pierwszav2(1234565678987654323))