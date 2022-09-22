#ZESTAW 5 MRÓZ KAMIL
import math

def euklides(licznik, mianownik):
    dzielnik = math.gcd(licznik, mianownik)
    return [licznik / dzielnik, mianownik / dzielnik]

def add_frac(frac1, frac2):         # frac1 + frac2
    return euklides(frac1[0]*frac2[1]+frac1[1]* frac2[0], frac1[1] * frac2[1])

def sub_frac(frac1, frac2):         # frac1 - frac2
    return euklides(frac1[0] * frac2[1] - frac1[1] * frac2[0], frac1[1] * frac2[1])

def mul_frac(frac1, frac2):         # frac1 * frac2
    return  euklides(frac1[0] * frac2[0], frac1[1] * frac2[1])

def div_frac(frac1, frac2):         # frac1 / frac2
    return euklides(frac1[0] * frac2[1], frac1[1] * frac2[0])

def is_positive(frac):              # bool, czy dodatni
    return frac[0] * frac[1] > 0

def is_zero(frac):                  # bool, typu [0, x]
    return frac[0] * frac[1] == 0

def cmp_frac(frac1, frac2):         # -1 | 0 | +1
    frac1 = float(frac1[0]/frac1[1])
    frac2 = float(frac2[0]/frac2[1])
    if frac1 < frac2:
        return -1
    elif frac1 > frac2:
        return 1
    else:
        return 0

def frac2float(frac):               # konwersja do float
    return float(frac[0]/frac[1])
