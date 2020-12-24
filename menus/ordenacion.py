from menus.menu import Menu

from ordenacion.binary_search import binary_search_i, binary_search_m
from ordenacion.encuentra_suma import encuentra_suma_max
from ordenacion.heap_sort import heap_sort
from ordenacion.insertion_sort import insertion_sort, linear_search
from ordenacion.merge_sort import merge_sort

from rich.console import Console

from typing import Dict, List

from utils.helpers import clear_screen, print_arr, wait_enter
from utils.input_helpers import confirmation, get_array, get_int


class MenuOrdenacion(Menu):
    def __init__(self, console: Console):
        super(MenuOrdenacion, self).__init__(console)
        self.arreglo = []
        self.arreglo_ordenado = []
        self.options = {
            '1': {
                'name': 'Insertion-sort',
                'fun': insertion_sort,
                'type': 'ord',
                'import': 'from ordenacion.insertion_sort import insertion_sort'
            },
            '2': {
                'name': 'Merge-sort',
                'fun': merge_sort,
                'type': 'ord',
                'import': 'from ordenacion.merge_sort import merge_sort'
            },
            '3': {
                'name': 'Heap-sort',
                'fun': heap_sort,
                'type': 'ord',
                'import': 'from ordenacion.heap_sort import heap_sort'
            },
            '7': {
                'name': 'Linear Search',
                'fun': linear_search,
                'params': [
                    {'name': 'el valor a encontrar'}
                ],
                'type': 'bus',
                'import': 'from ordenacion.insertion_sort import linear_search'
            },
            '8': {
                'name': 'Binary Search',
                'fun': binary_search_i,
                'params': [
                    {'name': 'el valor a encontrar'},
                    {'name': 'i', 'sup': 'len', 'inf': 0},
                    {'name': 'j', 'sup': 'len', 'inf': 0}
                ],
                'type': 'bus',
                'ordered': True,
                'import': 'from ordenacion.binary_search import binary_search_i'
            },
            '9': {
                'name': 'Binary Search (Max)',
                'fun': binary_search_m,
                'params': [
                    {'name': 'el valor a encontrar'},
                    {'name': 'i', 'sup': 'len', 'inf': 0},
                    {'name': 'j', 'sup': 'len', 'inf': 0}
                ],
                'type': 'bus',
                'ordered': True,
                'msg': 'El elemento máximo con respecto al valor dado es',
                'value': True,
                'import': 'from ordenacion.binary_search import binary_search_m'
            },
            '10': {
                'name': 'Encuentra suma máxima',
                'fun': encuentra_suma_max,
                'params': [
                    {'name': 'el valor a encontrar'}
                ],
                'type': 'bus',
                'ordered': True,
                'msg': 'El par de elementos cuya suma es máxima con respecto al valor dado son',
                'import': 'from ordenacion.encuentra_suma import encuentra_suma_max'
            },
            'total': 10
        }

    def start(self):
        while True:
            self.print_md_file('menu_ordenacion')
            self.console.print('Para salir del menú en el que se encuentre, presione "q"', justify='center')
            total = self.options['total']
            opc = get_int(f'¿Qué algoritmo desea utilizar? (1 a {total})', 1, total)
            if opc is None:
                if confirmation('Está por regresar al menú principal, ¿desea continuar?', self.console):
                    break
                else:
                    continue
            else:
                self.execute_algorithm(self.options[str(opc)])

    def execute_algorithm(self, algorithm: Dict):
        self.print_algorithm_menu(algorithm)
        self.set_arreglo()
        if algorithm['type'] == 'ord':
            self.exec_ord(algorithm)
        else:
            self.exec_bus(algorithm)
        wait_enter(self.console, 'para volver al menú de ordenación y búsqueda')

    def exec_ord(self, algorithm: Dict) -> None:
        params = self.get_params(algorithm.get('params', []))
        self.arreglo_ordenado = [n for n in self.arreglo]
        algorithm['fun'](self.arreglo_ordenado, *params)
        self.progressbar(algorithm, self.arreglo, params, 'Ordenando')
        self.console.print('El arreglo tras ejecutar el algoritmo: ')
        print_arr(self.arreglo_ordenado, 'Arreglo ordenado:')

    def exec_bus(self, algorithm: Dict):
        if algorithm.get('ordered', False):
            if not self.arreglo_ordenado:
                self.arreglo_ordenado = [n for n in self.arreglo]
                merge_sort(self.arreglo_ordenado)
            arr = self.arreglo_ordenado
            self.console.print(
                '\n**Dado que el algoritmo lo requiere, se utilizará la versión ordenada del arreglo**\n',
                justify='center',
                style='bold cyan'
            )
            print_arr(self.arreglo_ordenado, 'Arreglo ordenado:', self.console)
        else:
            arr = self.arreglo
        while True:
            params = self.get_params(algorithm.get('params', []))
            result = algorithm['fun'](arr, *params)
            self.progressbar(algorithm, self.arreglo, params, 'Buscando')
            if result is None:
                self.console.print('No se encontró el elemento buscado', justify='center', style='bold red')
            else:
                msg = algorithm.get('msg', 'El elemento se encuentra en la posición')
                result = arr[result] if algorithm.get('value', False) else result
                self.console.print(f'\n{msg}: {result}', style='bold green')
            if confirmation('¿Desea buscar otro valor?', self.console):
                self.print_algorithm_menu(algorithm, arr)
            else:
                break

    def print_algorithm_menu(self, algorithm: Dict, arreglo: List = None) -> None:
        clear_screen()
        self.print_md(f'# {algorithm["name"]}')
        if arreglo:
            print_arr(arreglo, 'Arreglo utilizado:', self.console)

    def set_arreglo(self):
        if self.arreglo:
            print_arr(self.arreglo, "Ya se había ingresado un arreglo:", self.console)
            if confirmation('¿desea seguir utilizando el mismo?'):
                return
        self.arreglo = get_array()
        self.arreglo_ordenado = []

    def get_params(self, params: List) -> List:
        values = []
        for param in params:
            values.append(get_int(
                msg=f"Ingrese {param['name']}",
                cota_inf=param.get('inf', None),
                cota_sup=self.get_cota_sup(param)
            ))
        return values

    def get_cota_sup(self, param: Dict) -> int:
        sup = param.get('sup', None)
        if sup == 'len':
            sup = len(self.arreglo) - 1
        return sup
