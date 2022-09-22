# Mróz Kamil Zestaw 4

# ZADANIE  4.2 / 3.5
def make_ruler(n):
    print("\n4.2 / 3.5\nProgram do rysowania miarki")
    dlugosc = int(n)
    miarka = ""
    liczby = ""
    pelnystring = str.join("\n ", (" " + miarka.join(["|...." for _ in range(0, dlugosc)]) + "|",
                                   "0" + liczby.join(["%5s" % (x + 1) for x in range(0, dlugosc)])))
    return pelnystring


# ZADANIE 4.2 / 3.6
def make_grid(rows, cols):
    print("\n4.2 / 3.6\nProgram rysujący prostokąt z małych kratek")
    wysokosc = int(rows)
    szerokosc = int(cols)
    pelnystring = ""
    for _ in range(0, wysokosc):
        pelnystring += "".join(["+---" for _ in range(0, szerokosc)]) + "+" + "\n"
        pelnystring += "".join(["|   " for _ in range(0, szerokosc)]) + "|" + "\n"
    pelnystring += "".join(["+---" for _ in range(0, szerokosc)]) + "+" + "\n"
    return pelnystring


# ZADANIE 4.3
def factorial(n):
    silnia = 1
    for x in range(2, n + 1):
        silnia = silnia * x
    return silnia


# ZADANIE 4.4
def fibonacci(n):
    if n == 0:
        return 0
    po = 0
    ob = 1
    for x in range(n - 1):
        po, ob = ob, po + ob
    return ob


# ZADANIE 4.5
def odwracanieite(L, left, right):
    while left <= right:
        temp = L[left]
        L[left] = L[right]
        L[right] = temp
        left += 1
        right -= 1
    return L


def odwracanierek(L, left, right):
    if left < right:
        temp = L[left]
        L[left] = L[right]
        L[right] = temp
        return odwracanierek(L, left + 1, right - 1)
    return L


# ZADANIE 4.6
def sum_seq(sequence):
    L = []
    for x in sequence:
        if isinstance(x, (list, tuple)):
            L.append(sum_seq(x))
        else:
            L.append(x)
    return sum(L)


# ZADANIE 4.7
def flatten(sequence):
    K = []
    for x in sequence:
        if isinstance(x, (list, tuple)):
            K.extend(flatten(x))
        else:
            K.append(x)
    return K


if __name__ == '__main__':
    # ZADANIE  4.2 / 3.5
    miar = 5
    print(make_ruler(miar))
    # ZADANIE 4.2 / 3.6
    row = 2
    col = 3
    print(make_grid(row, col))
    # ZADANIE 4.3
    sil = 7
    print("4.3\n", sil, "! jest równe", factorial(sil))
    # ZADANIE 4.4
    fib = 17
    print("\n4.4\n", fib, "-ty wyraz ciągu Fibonacciego jest równy:", fibonacci(fib))
    # ZADANIE 4.5
    Lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    lewa = 3
    prawa = 7
    print("\n4.5\nLista", Lista)
    print("Odwracanie elementów na liście iteracyjne:", odwracanieite(Lista, lewa, prawa))
    Lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("Odwracanie elementów na liście rekurencyjne:", odwracanierek(Lista, lewa, prawa))
    # ZADANIE 4.6
    sekwencja = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
    print("\n4.6\nSuma liczb zawartych w sekwencji z podsekwencjami", sekwencja, "wynosi:", sum_seq(sekwencja))
    # ZADANIE 4.7
    print("\n4.7\nSpłaszczona lista wszystkich elementów sekwencji", sekwencja, ":", flatten(sekwencja))
