import math

import os
import sys

from typing import List

from rich.console import Console
from rich.table import Table


def clear_screen():
    if sys.platform[:3] == 'win':
        os.system('cls')
    if sys.platform[:5] == 'linux' or sys.platform[:6] == 'darwin':
        os.system('clear')


def wait_enter(console, msg: str = 'para continuar'):
    console.input(f'\n\n[blink]Presione enter {msg}...[/]')


def print_arr(arr: List, title: str = "Arreglo", console: Console = None, limit: int = 25) -> None:
    if console is None:
        console = Console()
    cols = len(arr)
    rows = math.ceil(len(arr) / limit)
    if rows == 1:
        table = Table(title=title)
        table.add_column("i", justify="center", no_wrap=True)
        for col in range(cols):
            table.add_column(str(col), style="cyan")
        table.add_row("n", *[str(n) for n in arr])
        console.print(table, justify="center")
    else:
        for row in range(rows):
            if row == 0:
                title = f'{title} \nParte #{row + 1}'
            else:
                title = f'Parte #{row + 1}'
            table = Table(title=title)
            table.add_column("i", justify="center", no_wrap=True)
            printed_cols = min(cols, limit)
            cols -= limit
            for col in range(printed_cols):
                table.add_column(str(col + row*limit), style="cyan")
            table.add_row("n", *[str(n) for n in arr[row*limit:((row + 1) * limit)]])
            console.print(table, justify="center")
    print('\n')
