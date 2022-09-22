import random


# ZADANIE 8.1
def solve1(a, b, c):
    """Rozwiązywanie równania liniowego a x + b y + c = 0."""
    print("\n8.1 \n Rozwiązaniem równania liniowego", a, "x +", b, "y +", c, "= 0 jest:")
    if a == 0 and b == 0:
        if c == 0:
            print("Nieskończenie wiele rozwiązań")
            return
        else:
            print("Nie ma rozwiązania")
            return
    if a == 0:
        print(" y = ", -c / b)
    elif b == 0:
        print(" x = ", -c / a)
    else:
        print("y = -({0} * x + {1})/{2}".format(a, c, b))


# ZADANIE 8.3
def calc_pi(n):
    """Obliczanie liczby pi metodą Monte Carlo.
        n oznacza liczbę losowanych punktów."""
    pi = 0
    counter = 0
    for i in range(n):
        random_x = random.uniform(-1, 1)
        random_y = random.uniform(-1, 1)
        dst_org = (random_x ** 2 + random_y ** 2) ** (1 / 2)
        if dst_org <= 1:
            counter += 1
        pi = 4 * counter / n
    print("\n8.3\nLiczba Pi metodą Monte Carlo:", pi, "o", n, "losowań punktów")


# ZADANIE 8.4
def heron(a, b, c):
    """Obliczanie pola powierzchni trójkąta za pomocą wzoru
        Herona. Długości boków trójkąta wynoszą a, b, c."""
    if a + b > c and a + c > b and b + c > a:
        p = (a + b + c) / 2
        print("\n8.4\nPole powierzchni trójkąta o bokach", a, b, c, "wynosi: ",
              ((p * (p - a) * (p - b) * (p - c)) ** (1 / 2)))
    else:
        raise ValueError


# ZADANIE 8.6
def recursion(i, j):
    if i == 0 and j == 0:
        return 0.5
    if i > 0 and j == 0:
        return 0
    if i == 0 and j > 0:
        return 1
    if j > 0 and i > 0:
        return 0.5 * (recursion(i - 1, j) + recursion(i, j - 1))


def iteration(i, j):
    v = {(0, 0): 0.5}
    n = max(i, j)
    for x in range(n + 1):
        v[x, 0] = 0
        v[0, x] = 1

    for x in range(1, n + 1):
        for y in range(1, n + 1):
            v[x, y] = 0.5 * ((v[x - 1, y]) + v[(x, y - 1)])

    return v[(i, j)]


if __name__ == '__main__':
    solve1(0, 0, 0)
    solve1(0, 0, 6)
    solve1(0, 6, 3)
    solve1(0, -3, 6)
    solve1(3, 0, 3)
    solve1(3, 3, 3)

    calc_pi(10000)

    heron(10, 15, 20)
    heron(15, 20, 25)
