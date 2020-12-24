from typing import List, Union
import math


def binary_search_r(
    arr: List, x: Union[int, float], i: int, j: int
) -> Union[int, None]:
    m = math.ceil((i + j - 1)/2)
    if x == arr[m]:
        return m
    elif x < arr[m] and i < m:
        return binary_search_r(arr, x, i, m - 1)
    elif x > arr[m] and j > m:
        return binary_search_r(arr, x, m + 1, j)
    else:
        return None


def binary_search_i(
    arr: List, x: Union[int, float], i: int, j: int
) -> Union[int, None]:
    while i <= j:
        m = math.ceil((i + j - 1)/2)
        if x == arr[m]:
            return m
        elif x < arr[m] and i < m:
            j = m - 1
        elif x > arr[m] and j > m:
            i = m + 1
        else:
            return None


def binary_search_m(
    arr: List, x: Union[int, float], i: int, j: int, best: int = 0
) -> Union[int, None]:
    m = math.ceil((i + j - 1)/2)
    if x == arr[m]:
        return m
    elif (x - arr[m] > 0) and (x - arr[m] < x - arr[best]):
        best = m
    if x < arr[m]:
        if not i < m:
            if arr[best] > x:
                return None
            return best
        return binary_search_m(arr, x, i, m - 1, best)
    else:
        if not j > m:
            return best
        return binary_search_m(arr, x, m + 1, j, best)


# arr = [1,3,4,5,6,9,11,13,14,25]
# print(arr)
# print(binary_search_r(arr, 9, 0, len(arr) - 1))
# print(binary_search_r(arr, 10, 0, len(arr) - 1))
# print(binary_search_r(arr, 2, 0, len(arr) - 1))
# print(binary_search_r(arr, 9, 0, len(arr) - 1))
# print(binary_search_r(arr, 10, 0, len(arr) - 1))
# print(binary_search_i(arr, 13, 0, len(arr) - 1))
# print(binary_search_i(arr, 2, 0, len(arr) - 1))
# print(7, binary_search_m(arr, 7, 0, len(arr) - 1))
# print(2, binary_search_m(arr, 2, 0, len(arr) - 1))
# print(8, binary_search_m(arr, 8, 0, len(arr) - 1))
# print(10, binary_search_m(arr, 10, 0, len(arr) - 1))
# print(12, binary_search_m(arr, 12, 0, len(arr) - 1))
# print(16, binary_search_m(arr, 16, 0, len(arr) - 1))
# print(0, arr[binary_search_m(arr, 0, 0, len(arr) - 1)])
