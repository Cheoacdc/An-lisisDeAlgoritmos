import random

from typing import List

from utils.helpers import exchange


def partition(arr: List, p: int, r: int) -> int:
    x = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            exchange(arr, i, j)
    exchange(arr, i + 1, r)
    return i + 1


def quicksort(arr: List, p: int = 0, r: int = None) -> None:
    if r is None:
        r = len(arr) - 1
    if p < r:
        q = partition(arr, p, r)
        quicksort(arr, p, q - 1)
        quicksort(arr, q + 1, r)


def randomized_partition(arr: List, p: int, r: int) -> int:
    i = random.randint(p, r)
    exchange(arr, r, i)
    return partition(arr, p, r)


def randomized_quicksort(arr: List, p: int = 0, r: int = None) -> None:
    if r is None:
        r = len(arr) - 1
    if p < r:
        q = partition(arr, p, r)
        quicksort(arr, p, q - 1)
        quicksort(arr, q + 1, r)
