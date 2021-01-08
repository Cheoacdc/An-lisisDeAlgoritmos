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
