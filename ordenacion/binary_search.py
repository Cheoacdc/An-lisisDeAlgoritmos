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
