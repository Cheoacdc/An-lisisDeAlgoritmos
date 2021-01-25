import math

import os
import sys

from typing import Dict, List

from rich.console import Console
from rich.table import Table


def clear_screen():
    if sys.platform[:3] == 'win':
        os.system('cls')
    if sys.platform[:5] == 'linux' or sys.platform[:6] == 'darwin':
        os.system('clear')


def wait_enter(console, msg: str = 'para continuar'):
    console.input(f'\n\n[blink]Presione enter {msg}...[/]')


def print_arr(
        arr: List, title: str = "Arreglo", console: Console = None,
        limit: int = 25, cols_name: str = 'i', rows_name: str = 'n', i: int = 0
) -> None:
    if console is None:
        console = Console()
    cols = len(arr)
    rows = math.ceil(len(arr) / limit)
    if rows == 1:
        table = Table(title=title)
        table.add_column(cols_name, justify="center", no_wrap=True)
        for col in range(i, cols + i):
            table.add_column(str(col), style="cyan")
        table.add_row(rows_name, *[str(n) for n in arr])
        console.print(table, justify="center")
    else:
        for row in range(rows):
            if row == 0:
                title = f'{title} \nParte #{row + 1}'
            else:
                title = f'Parte #{row + 1}'
            table = Table(title=title)
            table.add_column(cols_name, justify="center", no_wrap=True)
            printed_cols = min(cols, limit)
            cols -= limit
            for col in range(printed_cols):
                table.add_column(str(col + row*limit), style="cyan")
            table.add_row(rows_name, *[str(n) for n in arr[row*limit:((row + 1) * limit)]])
            console.print(table, justify="center")
    print('\n')


def print_dict_arr(arr: List[Dict], keys: List[Dict], title: str = "Arreglo", console: Console = None) -> None:
    if console is None:
        console = Console()
    rows = len(arr)
    table = Table(title=title)
    table.add_column("i", justify="center", no_wrap=True)
    for key in keys:
        table.add_column(key['name'], style="cyan")
    for row in range(rows):
        table.add_row(str(row), *[str(arr[row][key['key']]) for key in keys])
    console.print(table, justify="center")
    print('\n')


def print_dict_graph(graph: Dict, keys: List[Dict], title: str = "Grafo", console: Console = None) -> None:
    if console is None:
        console = Console()
    table = Table(title=title)
    table.add_column("nodo", justify="center", no_wrap=True)
    for key in keys:
        table.add_column(key['name'], style="cyan")
    for node in graph:
        table.add_row(node, *[str(graph[node][key['key']]) for key in keys])
    console.print(table, justify="center")
    print('\n')


def exchange(arr: List, i: int, j: int) -> None:
    aux = arr[j]
    arr[j] = arr[i]
    arr[i] = aux
