from typing import List


def check_int(num: str) -> int or None:
    try:
        result = int(num)
    except ValueError:
        return None
    return result


def get_int(msg: str = 'Ingrese el valor') -> int:
    while True:
        n = check_int(input(f'{msg}: '))
        if n is None:
            print('**Ingrese un entero válido**\n')
        else:
            return n


def get_array() -> List:
    arr = []
    n = get_int('¿Cuántos elementos tiene el arreglo?')
    for i in range(0, n):
        val = get_int(f'Ingrese el valor del elemento #{i + 1}')
        arr.append(val)
    return arr
