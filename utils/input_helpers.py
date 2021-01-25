import numpy as np

from rich import print
from rich.console import Console

from typing import Dict, List, Union

from utils.errors import QuitException
from utils.helpers import print_arr, print_dict_arr


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


def get_str(msg: str = 'Ingrese el valor') -> str:
    while True:
        cadena = input(f'{msg}: ')
        if cadena == 'quit':
            raise QuitException()
        if cadena == '':
            print('No puede ingresar un espacio en blanco.')
            continue
        return cadena


def get_array(
        tipo: str = 'int',  msg: str = 'Ingrese el valor del elemento #', offset: bool = False,
        cols_name: str = 'i', rows_name: str = 'n'
) -> List or None:
    while True:
        n = get_int('¿Cuántos elementos tiene el arreglo?')
        if confirmation(f'n = {n}, ¿desea continuar?'):
            break
    if n is None:
        return None
    fun = get_int if tipo == 'int' else get_str
    while True:
        arr = [0] if offset else []
        for i in range(0, n):
            val = fun(f'{msg}{i + 1}')
            arr.append(val)
        print_arr(arr, 'El arreglo es: ', cols_name=cols_name, rows_name=rows_name)
        if confirmation():
            break
    return arr


def get_dict_array(keys: List[Dict]) -> List or None:
    while True:
        n = get_int('¿Cuántos elementos tiene el arreglo?')
        if confirmation(f'n = {n}, ¿desea continuar?'):
            break
    if n is None:
        return None
    while True:
        arr = []
        print('')
        for i in range(0, n):
            obj = {}
            for key in keys:
                input_str = f'Ingrese {key["msg"]} del elemento #{i + 1}'
                obj[key['key']] = get_int(input_str) if key['type'] == 'int' else get_str(input_str)
            arr.append(obj)
            print('')
        print_dict_arr(arr, keys=keys, title='El arreglo es: ')
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
