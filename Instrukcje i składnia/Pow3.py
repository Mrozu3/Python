# Mróz Kamil Zestaw 3

# ZADANIE 3.4
def pow3():
    print("\n3.4\nProgram wypisujący trzecią potęgę podanej liczby")
    liczba = ''
    while liczba != "stop":
        liczba = input("Podaj liczbę: ")
        try:
            if liczba == "stop":
                exit()
            else:
                liczba = float(liczba)
                print(liczba, "do trzeciej to ", pow(liczba, 3))
        except ValueError:
            print("Wpisano napis zamiast liczby, proszę podać liczbę lub wpisać \"stop\"")


if __name__ == '__main__':
    pow3()
