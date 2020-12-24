import math
import numpy as np

from typing import List


def merge(arr: List, p: int, q: int, r: int) -> None:
    n1 = q - p + 1
    n2 = r - q
    l_arr = []
    r_arr = []
    for i in range(n1):
        l_arr.append(arr[p + i])
    for j in range(n2):
        r_arr.append(arr[q + j + 1])
    l_arr.append(np.inf)
    r_arr.append(np.inf)
    i = j = 0
    for k in range(p, r + 1):
        if l_arr[i] <= r_arr[j]:
            arr[k] = l_arr[i]
            i += 1
        else:
            arr[k] = r_arr[j]
            j += 1


def merge_sort(arr: List, p: int = 0, r: int = None):
    if r is None:
        r = len(arr) - 1
    if p < r:
        q = math.floor((p + r)/2)
        merge_sort(arr, p, q)
        merge_sort(arr, q + 1, r)
        merge(arr, p, q, r)


arr = [5,3,4,9,7,5,6,8,4,1,3,4]
merge_sort(arr)
print(arr)
