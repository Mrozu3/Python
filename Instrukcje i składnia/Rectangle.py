# Mróz Kamil Zestaw 3

# ZADANIE 3.6
def rect():
    print("\n3.6\nProgram rysujący prostokąt z małych kratek")
    wysokosc = ''
    szerokosc = ''
    while szerokosc != "stop" or wysokosc != "stop":
        wysokosc = input("Podaj wysokość prostokąta: ")
        szerokosc = input("Podaj szerokość prostokąta: ")
        try:
            if szerokosc == "stop" or wysokosc == "stop":
                exit()
            else:
                wysokosc = int(wysokosc)
                szerokosc = int(szerokosc)
                pelnystring = ""
                for _ in range(0, wysokosc):
                    pelnystring += "".join(["+---" for _ in range(0, szerokosc)]) + "+" + "\n"
                    pelnystring += "".join(["|   " for _ in range(0, szerokosc)]) + "|" + "\n"
                pelnystring += "".join(["+---" for _ in range(0, szerokosc)]) + "+" + "\n"
                print(pelnystring)
        except ValueError:
            print("Wpisano napis zamiast liczby, proszę podać liczbę lub wpisać \"stop\"")


if __name__ == '__main__':
    rect()
