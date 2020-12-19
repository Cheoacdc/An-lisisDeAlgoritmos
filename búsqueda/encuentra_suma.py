from binary_search import binary_search_m


def encuentra_suma_max_while(A, y):
    bxi = 0
    bxj = 0
    j = 0
    while not bxi + bxj == y and j < len(A):
        i = binary_search_m(A, abs(y - A[j]), 0, len(A) - 1, 0)
        if A[i] + A[j] > bxi + bxj:
            bxi = A[i]
            bxj = A[j]
        j += 1
    return bxi, bxj


def encuentra_suma_max(A, y):
    bxi = 0
    bxj = 0
    j = 0
    for j in range(len(A)):
        i = binary_search_m(A, abs(y - A[j]), 0, len(A) - 1, 0)
        if A[i] + A[j] > bxi + bxj:
            bxi = A[i]
            bxj = A[j]
        if bxi + bxj == y:
            break
    return bxi, bxj


arr = [1, 2, 4, 5, 7, 9, 11]
print(encuentra_suma_max(arr, 70))
