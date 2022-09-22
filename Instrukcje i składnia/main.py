# Mróz Kamil Zestaw 3

# ZADANIE 3.3
print("\n3.3\nLiczby do 30 niepodzielne przez 3:\n", " ".join([str(x) for x in range(0, 30) if x % 3 != 0]))

# ZADANIE 3.8
print("\n3.8")
L1 = [1, 5, 6, 12, 6, 92, 14, 2, 4]
L2 = [0, 4, 6, 17, 0, 84, 145, 22, 41]
print("Lista elementów występujących jednocześnie w obu sekwencjach", set(L1).intersection(set(L2)))
print("Lista wszystkich elementów z obu sekwencji", set(L1).union(set(L2)))

# ZADANIE 3.9
print("\n3.9\nSuma liczb z sekwencji", list(map(lambda x: sum(x), [[], [4], (1, 2), [3, 4], (5, 6, 7)])))

# ZADANIE 3.10
print("\n3.10")
#Sposób 1
slownik = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
print(slownik)
#Sposób 2
slownik = dict([("I", 1), ("V", 5), ("X", 10), ("L", 50), ("C", 100), ("D", 500), ("M", 1000)])
print(slownik)

#Sposób 3
slownik = {}
slownik['I'] = 1
slownik['V'] = 5
slownik['X'] = 10
slownik['L'] = 50
slownik['C'] = 100
slownik['D'] = 500
slownik['M'] = 1000
print(slownik)

#Sposób 4
klucz = ["I", "V", "X", "L", "C", "D", "M"]
wartosc = [1, 5, 10, 50, 100, 500, 1000]
slownik = dict(zip(klucz, wartosc))
print(slownik)



