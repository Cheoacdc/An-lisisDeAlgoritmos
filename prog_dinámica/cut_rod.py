import numpy as np
from typing import List, Union


def memoized_cut_rod(p: List, n: int):
    r = np.zeros(n + 1)
    r.fill(-np.inf)
    return memoized_cut_rod_aux(p, n, r)


def memoized_cut_rod_aux(p: List, n: int, r: Union[List, np.ndarray]):
    if r[n] >= 0:
        return r[n]
    q = 0
    if not n == 0:
        q = -np.inf
        for i in range(0, n):
            q = max(q, p[i] + memoized_cut_rod_aux(p, n - i - 1, r))
    r[n] = q
    return q


prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
print(memoized_cut_rod(prices, 9))
