from typing import List
import numpy as np


def counting_sort(arr: List, k: int) -> None:
    snapshot_arr = [n for n in arr]
    aux_arr = np.zeros(k + 1, np.int)
    for j in range(len(arr)):
        aux_arr[arr[j]] += 1
    for i in range(1, k + 1):
        aux_arr[i] = aux_arr[i] + aux_arr[i - 1]
    j = len(arr) - 1
    while j >= 0:
        aux_arr[snapshot_arr[j]] -= 1
        arr[aux_arr[snapshot_arr[j]]] = snapshot_arr[j]
        j -= 1
