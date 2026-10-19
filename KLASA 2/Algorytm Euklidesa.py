#NWD
def NWD1(a, b):
    while a != b and b != 0:
        if a > b:
            a = a - b
        else:
            b = b - a
    if a > 0:
        return a
    else:
        return b

def NWD2(a, b):
    while a != b and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    if a > 0:
        return a
    else:
        return b

#NWW
def NWW(a, b):
    return a * b // NWD2(a, b)