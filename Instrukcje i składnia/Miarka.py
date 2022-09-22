# Mróz Kamil Zestaw 3

# ZADANIE 3.5
def measure():
    print("\n3.5\nProgram do rysowania miarki")
    dlugosc = ''
    while dlugosc != "stop":
        dlugosc = input("Podaj długość miarki: ")
        try:
            if dlugosc == "stop":
                exit()
            else:
                dlugosc = int(dlugosc)
                miarka = ""
                liczby = ""
                print(" " + miarka.join(["|...." for _ in range(0, dlugosc)]) + "|", "\n", "0" + liczby.join(["%5s" % (x+1) for x in range(0, dlugosc)]))
        except ValueError:
            print("Wpisano napis zamiast liczby, proszę podać liczbę lub wpisać \"stop\"")


if __name__ == '__main__':
    measure()
