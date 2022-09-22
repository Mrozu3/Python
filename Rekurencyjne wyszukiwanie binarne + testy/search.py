def binarne_rek(L, left, right, y):
    """Wyszukiwanie binarne w wersji rekurencyjnej."""
    if left <= right:
        middle = (left + right) // 2
        if L[middle] == y:
            return middle
        elif L[middle] > y:
            return binarne_rek(L, left, middle - 1, y)
        else:
            return binarne_rek(L, middle + 1, right, y)
    else:
        return None


def lider_py(L, left, right):
    S = {}
    for number in L[left:right]:
            if number not in S:
                S[number] = 1
            else:
                S[number] += 1
    c = max(S.values())
    if c > len(L[left:right]) / 2:
        for k, v in S.items():
            if v == c:
                return k
    else:
        return None    # na liście nie ma lidera
