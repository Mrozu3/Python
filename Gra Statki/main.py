# Mróz Kamil - po poprawkach
import random

# Zmienne Globalne
player_one = ""
opponent = ""
player_now = ""
ships_table = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]  # ZAKOMENTOWAĆ W CELU PRZYŚPIESZENIA ROZGRYWKI GRACZ KONTRA KOMPUTER
# ships_table = [3, 2, 1]  # USUNĄĆ KOMENTARZ, W CELU PRZYŚPIESZENIA ROZGRYWKI GRACZ KONTRA KOMPUTER

# Tablice trzymające lokalizacje statków
PLAYER_BOARD = [[" "] * 11 for i in range(11)]
COMPUTER_BOARD = [[" "] * 11 for i in range(11)]
PLAYER_GUESS_BOARD = [[" "] * 11 for i in range(11)]
COMPUTER_GUESS_BOARD = [[" "] * 11 for i in range(11)]

# Słowniki
letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}
numbers_to_letters = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J'}


def battlefield(board):
    """ Rysowanie planszy """
    print("   A B C D E F G H I J")
    print("  |_|_|_|_|_|_|_|_|_|_|")
    row_number = 1
    for row in board:
        if row_number == 10:
            print("%d|%s" % (row_number, "|".join(row)))
            break
        print("%d |%s" % (row_number, "|".join(row)))
        row_number += 1


def start_game():
    """ Wstęp do gry """
    global player_one

    print("\nWitaj w grze w Statki! Powiedz jak się nazywasz.")
    player_one = input("➤ Wpisz swoją nazwę: ")
    print("\nAdmirale {player_one}! Kto ma stanąć do walki z Kapitanem Czarnobrodym? "
          "Ty czy komputer?".format(player_one=player_one))
    settings()


def settings():
    """ Ustawienia gry """
    global opponent

    opponent = input("➤ Wybierz przedstawiciela: ").upper()  # WYBÓR PRZECIWNIKA

    if opponent == "JA":
        print("\nStaniesz do walki z Czarnobrodym \n Zasady są proste - zestrzel wszystkie "
              "okręty przeciwnika nim on zestrzeli Twoje")
        print(f"Admirał {player_one} kontra Czarnobrody!".format(player_one=player_one))
        print("\nZaczyna gracz {player_one}".format(player_one=player_one))
        pve()

    elif opponent == "KOMPUTER":
        print(
            "\n Zasady są proste - wygra ten komputer, który pierwszy zestrzeli wszystkie statki przeciwnika! "
            "\nStrzały oddawać będą naprzemiennie. Po każdym ruchu zostanie wyświetlona plansza. ")
        eve()

    else:
        print("\nAdmirale {player_one} opcje są dwie! Komputer czy drugi gracz?".format(player_one=player_one))
        settings()


def pve():
    """ Gracz kontra komputer"""
    global player_now

    player_board_creator(PLAYER_BOARD)
    player_now = "KOMPUTER"
    print("\nKomputer rozstawia statki na swojej planszy....")
    computer_board_creator(COMPUTER_BOARD)
    print("Komputer rozstawił wszystkie statki. Zaczynajmy bitwę!")


def eve():
    """ Komputer kontra komputer"""
    global player_now

    print("Admirał Michiel Adriaenszoon de Ruyter kontra Kapitan Czarnobrody!")
    computer_board_creator(PLAYER_BOARD)
    player_now = "KOMPUTER"
    computer_board_creator(COMPUTER_BOARD)


def player_board_creator(board):
    """ Tworzenie planszy dla Gracza"""
    global player_one

    battlefield(board)

    for ship in ships_table:
        print("\nStatki nie mogą się stykać i umieszczać je możesz tylko w poziomie lub pionie w granicach planszy. Aby"
              " ustawić statek podaj pola w których będzie się on znajdował (np. E1-E5, A1-A1)"
              " \nRozmiar statku jaki należy wstawić zostanie wyświetlony przed każdym rozmieszczeniem."
              " \nWpisz \"exit\", aby wyjść ")

        print("\n🛥🛥🛥🛥 {ship}-masztowiec 🛥🛥🛥🛥".format(ship=ship))
        start_column, start_row, end_column, end_row = set_the_ships()
        size = ship
        draw_board(board, start_column, start_row, end_column, end_row, size)

        print(f"\nPlansza gracza {player_one}".format(player_one=player_one))
        battlefield(board)


def computer_board_creator(board):
    """ Tworzenie planszy dla Komputera"""

    global player_now

    for ship in ships_table:
        if opponent != "JA":
            print("\n🛥🛥🛥🛥 {ship} masztowiec 🛥🛥🛥🛥".format(ship=ship))

        start_column, start_row, end_column, end_row = roll_the_ships()
        size = ship
        draw_board(board, start_column, start_row, end_column, end_row, size)

        if player_now == "KOMPUTER" and opponent != "JA":
            print(f"\nPlansza Kapitana Czarnobrodego")
        elif opponent != "JA":
            print(f"\nPlansza Admirała Michiel Adriaenszoon de Ruyter")

        if opponent != "JA":
            battlefield(board)


def set_the_ships():
    """ Odczytywanie położenia statków"""
    while True:
        ship = input("\n➤ Umieść statek na planszy: ").upper()

        if ship == "EXIT":
            exit()
        else:
            try:
                start_coords, end_coords = ship.split("-")
            except ValueError:
                print("Niepoprawne dane")
            else:
                if check_coords(start_coords) and check_coords(end_coords):
                    start_row, start_column = set_coords(start_coords)
                    end_row, end_column = set_coords(end_coords)
                    break
            print("Niepoprawne umieszczenie")

    return start_column, start_row, end_column, end_row


def check_coords(coords):
    """ Sprawdzanie poprawności wprowadzonych ciągów """
    return (len(coords) == 2 and coords[0] in 'ABCDEFGHIJ' and coords[1] in '123456789') or \
           (len(coords) == 3 and coords[2] == '0' and coords[0] in 'ABCDEFGHIJ' and coords[1] in '123456789')


def set_coords(coords):
    """ Interpretacja współrzędnych """
    coords = list(coords)
    if len(coords) == 2 and coords[0] in 'ABCDEFGHIJ' and coords[1] in '123456789':
        column = letters_to_numbers[coords[0]]
        row = int(coords[1]) - 1
        # print(column, row)
        return row, column
    if len(coords) == 3 and coords[2] == '0' and coords[0] in 'ABCDEFGHIJ' and coords[1] in '123456789':
        coords[1] = '9'
        column = letters_to_numbers[coords[0]]
        row = int(coords[1])
        return row, column


def roll_the_ships():
    """ Losowanie rozmieszczenia statków komputera """
    temp = random.randrange(0, 99)
    start_column, start_row, end_column, end_row = 0, 0, 0, 0

    if temp < 50:
        start_column = random.randrange(0, 10)
        end_column = start_column
        start_row = random.randrange(0, 10)
        end_row = random.randrange(0, 10)

    if temp >= 50:
        start_row = random.randrange(0, 10)
        end_row = start_row
        start_column = random.randrange(0, 10)
        end_column = random.randrange(0, 10)

    return start_column, start_row, end_column, end_row


def draw_board(board, start_column, start_row, end_column, end_row, size):
    """ Rysowanie statków w tablicy"""
    # print("To jest draw_board", start_column, start_row, end_column, end_row)

    if check_correct(board, start_column, start_row, end_column, end_row, size):
        if start_row == end_row and start_column == end_column:  # JEDNO POLE
            board[start_row][start_column] = "X"

        if start_row == start_row and start_column != end_column:  # W POZIOMIE
            temp = 0
            while not start_column + temp == end_column:
                board[start_row][start_column + temp] = "X"
                board[end_row][end_column] = "X"
                temp = temp + 1

        if start_column == end_column and start_row != end_row:  # W PIONIE
            temp = 0
            while not start_row + temp == end_row:
                board[start_row + temp][start_column] = "X"
                board[end_row][end_column] = "X"
                temp = temp + 1
        # print("Narysowałem")


def check_correct(board, start_column, start_row, end_column, end_row, size):
    """ Sprawdzanie poprawności rozmieszczenia statków"""
    global player_now

    # print("Sprawdzam check_space")
    # print("Jestem w check_space", start_column, start_row, end_column, end_row, "ROZMIAR:", size)

    flag = True

    if size == 1:  # JEŚLI ROZMIAR JEST 1
        if start_row != end_row or start_column != end_column:
            if opponent == "JA" and player_now != "KOMPUTER":
                print("Nieprawidłowy rozmiar statku")
            flag = False

    if (end_column - start_column) + 1 != size and (end_row - start_row) + 1 != size:  # JEŚLI JEST ZŁEGO ROZMIARU
        if opponent == "JA" and player_now != "KOMPUTER":
            print("Nieprawidłowy rozmiar statku")
        flag = False

    if start_column != end_column and start_row != end_row:  # NIE JEST POZIOMO ANI PIONOWO
        if opponent == "JA" and player_now != "KOMPUTER":
            print("Statki mogą być ułożone tylko poziomo lub pionowo")
        flag = False

    if start_column > end_column or start_row > end_row:  # GDZIE POCZĄTEK, A GDZIE KONIEC
        if opponent == "JA" and player_now != "KOMPUTER":
            print("Najpierw podaj dziób statku, a potem rufę")
        flag = False

    if start_row == end_row and start_column == end_column:  # JEDNO POLE

        if board[start_row][start_column] == "X" or board[start_row + 1][start_column] == "X" or board[start_row - 1][
            start_column] == "X" or board[start_row][start_column + 1] == "X" or board[start_row][
            start_column - 1] == "X" \
                or board[start_row + 1][start_column - 1] == "X" or board[start_row + 1][start_column + 1] == "X" or \
                board[start_row - 1][start_column - 1] == "X" or board[start_row - 1][start_column + 1] == "X":
            if opponent == "JA" and player_now != "KOMPUTER":
                print("To pole jest już zajęte")
            flag = False

    if start_row == start_row and start_column != end_column:  # W POZIOMIE

        temp = 0
        while not start_column + temp > end_column:
            if board[start_row][start_column + temp] == "X" or board[start_row + 1][start_column + temp] == "X" or \
                    board[start_row - 1][start_column + temp] == "X" or board[start_row][start_column - 1] == "X" or \
                    board[start_row][end_column + 1] == "X" or board[start_row + 1][end_column + 1] == "X" or \
                    board[start_row - 1][end_column + 1] == "X" or board[start_row + 1][start_column - 1] == "X" or \
                    board[start_row - 1][start_column - 1] == "X":
                # print("To pola są zajęte dla poziomu")
                if opponent == "JA" and player_now != "KOMPUTER":
                    print("Te pola są już zajęte")
                flag = False

            temp = temp + 1

    if start_column == end_column and start_row != end_row:  # W PIONIE

        temp = 0
        while not start_row + temp > end_row:
            if board[start_row + temp][start_column] == "X" or board[start_row + temp][start_column + 1] == "X" or \
                    board[start_row + temp][start_column - 1] == "X" or board[end_row + 1][start_column] == "X" or \
                    board[start_row - 1][start_column] == "X" or board[start_row - 1][end_column - 1] == "X" or \
                    board[start_row - 1][end_column + 1] == "X" or board[end_row + 1][end_column - 1] == "X" or \
                    board[end_row + 1][end_column + 1] == "X":
                # print("Te pola są zajęte dla pionu")
                if opponent == "JA" and player_now != "KOMPUTER":
                    print("Te pola są już zajęte")
                flag = False

            temp = temp + 1

    if not flag:
        if opponent == "JA" and player_now != "KOMPUTER":
            start_column, start_row, end_column, end_row = set_the_ships()
            draw_board(board, start_column, start_row, end_column, end_row, size)
        if opponent == "KOMPUTER" or player_now == "KOMPUTER":
            start_column, start_row, end_column, end_row = roll_the_ships()
            draw_board(board, start_column, start_row, end_column, end_row, size)
    else:
        return flag


def player_hit():
    """ Strzały oddawane przez gracza"""
    while True:
        ship = input("\n➤ Podaj pole do ostrzału: ").upper()
        # print(coords)
        # print(len(coords))

        if ship == "EXIT":
            exit()

        if ship == "MOJE STATKI":
            print("Twoje statki")
            battlefield(PLAYER_BOARD)

        if ship == "TRAFIENIA KOMPUTERA":
            print("Plansza trafień przeciwnika")
            battlefield(COMPUTER_GUESS_BOARD)

        if ship == "OSZUSTWO":
            print("Plansza statków Czarnobrodego")
            battlefield(COMPUTER_BOARD)

        else:
            if check_coords(ship):
                row, column = set_coords(ship)
                break

        print("Niepoprawny cel")

    return row, column


def count_hit_ships(board):
    """ Sprawdzanie czy wszystkie statki został trafione"""
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count


def clean():
    """ Czyści ostatnią kolumnę """
    for x in range(0, 10):
        PLAYER_GUESS_BOARD[x][10] = ""
        COMPUTER_GUESS_BOARD[x][10] = ""


if __name__ == '__main__':
    start_game()
    print("\nNiech rozpocznie się bitwa!")

    win_condition = 0
    for i in range(0, len(ships_table)):
        win_condition = win_condition + ships_table[i]

    print("Warunkiem wygranej jest zestrzelenie wszytkich", win_condition, "pól okrętów przeciwnika. \n          "
                                                                           "     ***POMOC***")
    print("Możesz zobaczyć swoją planszę wpisując \"Moje statki\" \n Plansza trafień przeciwnika \"Trafienia "
          "Komputera\" \n Pssssst - Małe oszustwo? Wpisz \"OSZUSTWO\"")
    print("W celu wyrównania szans w rozgrywce Gracz kontra Komputer, gracz nie jest informowany czy okręt "
          "został w pełni zatopiony!")

    while True:

        # GRACZ KONTRA KOMPUTER
        if opponent == "JA":

            while True:  # TURA GRACZA
                print('\nWybierz jedno pole do ostrzelenia (np. E5)')
                battlefield(PLAYER_GUESS_BOARD)
                row, column = player_hit()
                if PLAYER_GUESS_BOARD[row][column] == "-" or PLAYER_GUESS_BOARD[row][column] == "X":
                    print("To pole zostało już ostrzelane.")
                elif COMPUTER_BOARD[row][column] == "X":
                    print("Trafiony!")
                    PLAYER_GUESS_BOARD[row][column] = "X"
                    break
                else:
                    print("Pudło!")
                    PLAYER_GUESS_BOARD[row][column] = "-"
                    break
            if count_hit_ships(PLAYER_GUESS_BOARD) == win_condition:
                print("Wygrałeś!")
                print("Plansza Twoich statków")
                battlefield(PLAYER_BOARD)
                print("Plansza trafień przeciwnika")
                battlefield(COMPUTER_GUESS_BOARD)
                break
        # KOMPUTER KONTRA KOMPTUER
        else:
            while True:  # TURA KOMPUTERA1
                row, column = random.randrange(0, 10), random.randrange(0, 10)
                while PLAYER_GUESS_BOARD[row][column] == "-" or PLAYER_GUESS_BOARD[row][column] == "X":
                    row, column = random.randrange(0, 10), random.randrange(0, 10)
                if COMPUTER_BOARD[row][column] == "X":
                    print("\nAdmirał Michiel Adriaenszoon de Ruyter trafił statek Czarnobrodego na polu "
                          "{column}{row}!".format(row=row + 1, column=numbers_to_letters[column]))
                    PLAYER_GUESS_BOARD[row][column] = "X"
                    PLAYER_GUESS_BOARD[row - 1][column - 1] = "-"
                    PLAYER_GUESS_BOARD[row + 1][column - 1] = "-"
                    PLAYER_GUESS_BOARD[row - 1][column + 1] = "-"
                    PLAYER_GUESS_BOARD[row + 1][column + 1] = "-"
                    clean()
                    battlefield(PLAYER_GUESS_BOARD)
                    break
                else:
                    PLAYER_GUESS_BOARD[row][column] = "-"
                    print("\nAdmirał Michiel Adriaenszoon de Ruyter chybił pole "
                          "{column}{row}!".format(row=row + 1, column=numbers_to_letters[column]))
                    break
            if count_hit_ships(PLAYER_GUESS_BOARD) == win_condition:
                print("Admirał Michiel Adriaenszoon de Ruyter wygrał w Twoim imieniu!")
                break

        # TURA KOMPUTERA
        while True:
            row, column = random.randrange(0, 10), random.randrange(0, 10)
            while COMPUTER_GUESS_BOARD[row][column] == "-" or COMPUTER_GUESS_BOARD[row][column] == "X":
                row, column = random.randrange(0, 10), random.randrange(0, 10)
            if PLAYER_BOARD[row][column] == "X":
                print("\nCzarnobrody trafił Twój statek na polu "
                      "{column}{row}!".format(row=row + 1, column=numbers_to_letters[column]))
                COMPUTER_GUESS_BOARD[row][column] = "X"
                COMPUTER_GUESS_BOARD[row - 1][column - 1] = "-"
                COMPUTER_GUESS_BOARD[row + 1][column - 1] = "-"
                COMPUTER_GUESS_BOARD[row - 1][column + 1] = "-"
                COMPUTER_GUESS_BOARD[row + 1][column + 1] = "-"
                clean()
                battlefield(COMPUTER_GUESS_BOARD)
                break
            else:
                COMPUTER_GUESS_BOARD[row][column] = "-"
                print("\nCzarnobrody chybił pole {column}{row}!".format(row=row + 1, column=numbers_to_letters[column]))
                break
        if count_hit_ships(COMPUTER_GUESS_BOARD) == win_condition:
            print("Czarnobrody wygrał!")
            break
