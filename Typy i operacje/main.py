#Mróz Kamil

line = "Lorem ipsum \n GvR dolor sit     amet."
word = "word"

print("\n", line, "\n")

#ZADANIE 2.10
print("2.10\nLiczba wyrazów w napisie:", len(line.split()))

#ZADANIE 2.11
word_ = ""

for char in word[0:len(word)]:
    word_ += char + "_"

word_ = word_[:-1]
print("\n2.11\nNapis rozdzielony znakami podkreslenia:", word_)

#ZADANIE 2.12
L = []
for x in line.split():
    L.append(x[0])

print("\n2.12\nNapis z pierwszych znaków wyrazów:", "".join(L))

L = []
for x in line.split():
    L.append(x[len(x)-1])

print("Napis z ostatnich znaków wyrazów:", "".join(L))

#ZADANIE 2.13
L = []
for x in line.split():
    L.append(len(x))

print("\n2.13\nSuma długości wyrazów:", sum(L))

#ZADANIE 2.14
print("\n2.14\nNajdłuższy wyraz: \"", sorted(line.split(), key=len, reverse=True)[0], "\" ma długość:", len(sorted(line.split(), key=len, reverse=True)[0]))

#ZADANIE 2.15
L = (1, 2, 4, 7, 8, 16, 32, 64, 128, 256, 512)
string = ""
for x in L:
    string = string + str(x)

print("\n2.15\nNapis będący ciągiem cyfr: ", string, type(string))

#ZADANIE 2.16
line = (line.replace("GvR", "Guido van Rossum"))
print("\n2.16\nZamieniony ciąg znaków:", line)

#ZADANIE 2.17
print("\n2.17\nAlfabetyczne posortowanie:", sorted(line.split(), key=str.lower), "\nSortowanie względem długości:", sorted(line.split(), key=len))

#ZADANIE 2.18
bignumber = 123000123000
print("\n2.18\nLiczba wystpąpień zer:", str(bignumber).count("0"))

#ZADANIE 2.19
block = ""
for x in L:
    block += " " + str(x).zfill(3)

print("\n2.19\nUzupełnienie do trzech:", block)
