import numpy as np
from typing import List, Tuple, Union


def memoized_cut_rod(p: List, n: int) -> Tuple:
    r = np.zeros(n + 1)
    r.fill(-np.inf)
    return memoized_cut_rod_aux(p, n, r), r


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


def extended_buttom_up_cut_rod(p: List, n: int, r: Union[List, np.ndarray], s: Union[List, np.ndarray]):
    for j in range(1, n + 1):
        q = -np.inf
        if r[j] == 0:
            for i in range(1, j + 1):
                if q <= p[i] + r[j - i]:
                    q = p[i] + r[j - i]
                    s[j] = i
            r[j] = q


def build_cut_rod_solution(p: List, n: int, r: Union[List, np.ndarray], s: Union[List, np.ndarray]) -> Tuple:
    if not r or not len(r) == len(p):
        r = np.zeros(len(p))
    if not s or not len(s) == len(p):
        s = np.zeros(len(p), dtype=int)
    extended_buttom_up_cut_rod(p, n, r, s)
    price = r[n]
    cuts = []
    while n > 0:
        cuts.append(s[n])
        n -= s[n]
    return price, cuts
