import numpy as np

from rich import print
from rich.console import Console

from typing import List, Union

from utils.errors import QuitException
from utils.helpers import print_arr


def check_int(num: str) -> int or None:
    try:
        result = int(num)
    except ValueError:
        return None
    return result


def get_int(msg: str = 'Ingrese el valor', cota_inf: int = None, cota_sup: int = None) -> int or None:
    cota_inf = -np.inf if cota_inf is None else cota_inf
    cota_sup = np.inf if cota_sup is None else cota_sup
    while True:
        n = input(f'{msg}: ')
        if n == 'q' or n == 'quit':
            raise QuitException()
        n = check_int(n)
        if n is None:
            print('[bold red]**Ingrese un entero válido**[/]\n')
        elif n < cota_inf or n > cota_sup:
            print(f'[bold red]El valor debe estar entre {cota_inf} y {cota_sup}[/]')
        else:
            return n


def get_array() -> List or None:
    while True:
        n = get_int('¿Cuántos elementos tiene el arreglo?')
        if confirmation(f'n = {n}, ¿desea continuar?'):
            break
    if n is None:
        return None
    while True:
        arr = []
        for i in range(0, n):
            val = get_int(f'Ingrese el valor del elemento #{i + 1}')
            arr.append(val)
        print_arr(arr, 'El arreglo es: ')
        if confirmation():
            break
    return arr


def confirmation(msg: str = '¿Desea continuar?', console: Union[Console, None] = None) -> bool:
    while True:
        if console:
            respuesta = console.input(f'[bold green]{msg} \[y/n]: ')
        else:
            respuesta = input(f'{msg} [y/n]: ')
        if respuesta.lower() == 'y' or respuesta == '':
            return True
        elif respuesta.lower() == 'n':
            return False
        else:
            print('[blink red]Ingrese una opción aceptada...\n')
            continue