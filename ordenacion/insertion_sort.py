from typing import List, Union


def insertion_sort(A: List) -> None:
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key


def linear_search(A: List, v: int) -> Union[int, None]:
    for j in range(len(A)):
        if A[j] == v:
            return j
        else:
            j += 1
