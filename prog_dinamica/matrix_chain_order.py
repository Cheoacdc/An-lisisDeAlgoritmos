import numpy as np

from typing import List, Tuple


def matrix_chain_order(dims: List[int]) -> Tuple:
    n = len(dims) - 1
    costs = np.zeros((n, n))
    indices = np.zeros((n, n), dtype=int)
    for l in range(1, n):
        for i in range(0, n - l):
            j = i + l
            costs[i, j] = np.inf
            for k in range(i, j):
                q = costs[i, k] + costs[k + 1, j] + dims[i]*dims[k + 1]*dims[j + 1]
                if q < costs[i, j]:
                    costs[i, j] = q
                    indices[i, j] = k
    return costs, indices


def build_optimal_parenthesis(s: np.array, i: int, j: int):
    sol = ''
    if i == j:
        sol += f'A{i + 1}'
    else:
        sol += '('
        sol += build_optimal_parenthesis(s, i, s[i, j])
        sol += build_optimal_parenthesis(s, s[i, j] + 1, j)
        sol += ')'
    return sol
