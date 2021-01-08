import numpy as np

from typing import List


def lcs_length(arr1: List, arr2: List):
    m = len(arr1)
    n = len(arr2)
    arr_b = np.zeros((m, n))
    arr_c = np.zeros((m + 1, n + 1))
    for i in range(0, m):
        for j in range(0, n):
            if arr1[i] == arr2[j]:
                arr_c[i + 1, j + 1] = arr_c[i, j] + 1
                arr_b[i, j] = 7
            elif arr_c[i, j + 1] >= arr_c[i + 1, j]:
                arr_c[i + 1, j + 1] = arr_c[i, j + 1]
                arr_b[i, j] = 8
            else:
                arr_c[i + 1, j + 1] = arr_c[i + 1, j]
                arr_b[i, j] = 4
    return arr_c, arr_b


def build_lcs(arr_b, arr_1, i, j, sol: List):
    if i < 0 or j < 0:
        return
    if arr_b[i, j] == 7:
        build_lcs(arr_b, arr_1, i - 1, j - 1, sol)
        sol.append(arr_1[i])
    elif arr_b[i, j] == 8:
        build_lcs(arr_b, arr_1, i - 1, j, sol)
    else:
        build_lcs(arr_b, arr_1, i, j - 1, sol)
