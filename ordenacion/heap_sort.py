import math

from typing import List

from utils.helpers import exchange


def left_of(i: int) -> int:
    return 2*(i + 1) - 1


def right_of(i: int) -> int:
    return 2 * (i + 1)


def max_heapify(arr: List, i: int, heapsize: int) -> None:
    left = left_of(i)
    right = right_of(i)
    largest = left if left <= heapsize and arr[left] > arr[i] else i
    largest = right if right <= heapsize and arr[right] > arr[largest] else largest
    if not largest == i:
        exchange(arr, i, largest)
        max_heapify(arr, largest, heapsize)


def build_max_heap(arr: List) -> int:
    heapsize = len(arr) - 1
    i = math.floor(heapsize/2)
    while i >= 0:
        max_heapify(arr, i, heapsize)
        i -= 1
    return heapsize


def heap_sort(arr: List) -> None:
    heapsize = build_max_heap(arr)
    while heapsize > 0:
        exchange(arr, 0, heapsize)
        heapsize -= 1
        max_heapify(arr, 0, heapsize)

