from typing import Dict, List

from ordenacion.merge_sort import merge_sort_dict


def activity_selector(arr: List[Dict], i: int = 0, result: List[Dict] = None):
    if i == 0:
        merge_sort_dict(arr, key='end')
    result = result if result else [arr[i]]
    n = len(arr) - 1
    m = i + 1
    while m <= n and arr[m]['start'] < arr[i]['end']:
        m += 1
    if m <= n:
        result.append(arr[m])
        activity_selector(arr, m, result)
    if i == 0:
        return result


def greedy_activity_selector(arr: List[Dict]):
    merge_sort_dict(arr, key='end')
    k = 0
    result = [arr[k]]
    for m in range(1, len(arr)):
        if arr[m]['start'] >= arr[k]['end']:
            result.append(arr[m])
            k = m
    return result


activities = [
    {'start': 1, 'end': 4},
    {'start': 8, 'end': 12},
    {'start': 2, 'end': 13},
    {'start': 3, 'end': 5},
    {'start': 8, 'end': 11},
    {'start': 0, 'end': 6},
    {'start': 5, 'end': 7},
    {'start': 12, 'end': 14},
    {'start': 3, 'end': 8},
    {'start': 5, 'end': 9},
    {'start': 6, 'end': 10}
]
