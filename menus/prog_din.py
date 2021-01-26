import time

from menus.menu import Menu

from prog_dinamica.cut_rod import build_cut_rod_solution
from prog_dinamica.lcs import build_lcs, lcs_length
from prog_dinamica.matrix_chain_order import matrix_chain_order, build_optimal_parenthesis


from rich.console import Console
from rich.table import Table

from typing import Dict, List

from utils.errors import QuitException
from utils.helpers import print_arr, wait_enter
from utils.input_helpers import confirmation, get_array, get_int


class MenuProgDin(Menu):
    def __init__(self, console: Console):
        super(MenuProgDin, self).__init__(console)
        self.options = {
            '1': {
                'name': 'Sucesión Común Más Larga',
                'fun': self.execute_lcs,
                'description': 'lcs'
            },
            '2': {
                'name': 'Orden de multiplicación de matrices',
                'fun': self.matrix_menu,
                'description': 'matrices'
            },
            '3': {
                'name': 'Cortado de Varillas',
                'fun': self.cut_rod_menu,
                'description': 'cut_rod'
            },
        }

    def start(self):
        while True:
            self.print_md_file('menu_prog_dinamica')
            total = len(self.options)
            try:
                opc = get_int(f'¿Qué algoritmo desea utilizar? (1 a {total})', 1, total)
            except QuitException:
                if confirmation('Está por regresar al menú principal, ¿desea continuar?', self.console):
                    break
                else:
                    continue
            try:
                self.execute_algorithm(self.options[str(opc)])
            except QuitException:
                self.console.print('Regresando al menú de programación dinámica...', style='bold red')
                time.sleep(1)

    def execute_algorithm(self, algorithm: Dict):
        if confirmation('¿Desea ver la descripción del algoritmo?', self.console):
            self.print_description(algorithm)
            wait_enter(self.console, 'para proceder al menú del algoritmo')
        algorithm['fun'](algorithm)
        wait_enter(self.console, 'para volver al menú de programación dinámica')

    def execute_lcs(self, algorithm: Dict):
        self.print_algorithm_menu(algorithm)
        self.console.print('Para el primer arreglo...', style='cyan', justify='center')
        arr1 = get_array(tipo='str')
        self.console.print('\nPara el segundo arreglo...', style='cyan', justify='center')
        arr2 = get_array(tipo='str')
        c, b = lcs_length(arr1, arr2)
        sol = []
        build_lcs(b, arr1, len(arr1) - 1, len(arr2) - 1, sol)
        if sol:
            print_arr(sol, 'La sucesión más larga es:', self.console)
        else:
            self.console.print(
                'No se encontraron elementos en la unión de los arreglos', style='bold red', justify='center'
            )

    def matrix_menu(self, algorithm: Dict):
        self.print_algorithm_menu(algorithm)
        dims = self.get_dimensions_array()
        (costs, indices) = matrix_chain_order(dims)
        self.execute_matrix(dims, indices)
        while True:
            if confirmation('¿Desea buscar para con otros límites?', self.console):
                self.print_algorithm_menu(algorithm)
                self.print_matrix_dims(dims)
                self.execute_matrix(dims, indices)
            else:
                break

    def execute_matrix(self, dims: List, indices: List):
        i = get_int('Ingrese el índice de la primer matriz a multiplicar', cota_inf=1, cota_sup=(len(dims) - 1))
        j = get_int('Ingrese el índice de la última matriz a multiplicar', cota_inf=i, cota_sup=(len(dims) - 1))
        sol = build_optimal_parenthesis(indices, i - 1, j - 1)
        self.console.print(f'\nLa manera óptima de colocar paréntesis es: [cyan]{sol}')

    def get_dimensions_array(self):
        while True:
            n = get_int('¿Cuántos matrices desea multiplicar?') + 1
            if confirmation(f'n = {n - 1}, ¿desea continuar?'):
                break
        while True:
            arr = [get_int('Ingrese el número de filas de A1')]
            for i in range(1, n):
                val = get_int(f'Ingrese el número de columnas de A{i}')
                arr.append(val)
            self.print_matrix_dims(arr)
            if confirmation():
                break
        return arr

    def print_matrix_dims(self, dims: List):
        rows = len(dims) - 1
        table = Table(title='Dimensiones de las matrices')
        table.add_column('.', justify="center", no_wrap=True)
        table.add_column('Filas', justify="center", style='cyan', no_wrap=True)
        table.add_column('Columnas', justify="center", style='cyan', no_wrap=True)
        for row in range(rows):
            table.add_row(f'A{row + 1}', str(dims[row]), str(dims[row + 1]))
        self.console.print(table, justify="center")

    def cut_rod_menu(self, algorithm: Dict):
        self.print_algorithm_menu(algorithm)
        arr = get_array(
            msg='Ingrese el costo de una varilla de longitud ', offset=True, cols_name='Longitud', rows_name='Precio'
        )
        prices = []
        cuts = []
        self.execute_cut_rod(arr, prices, cuts)
        while True:
            if confirmation('¿Desea buscar el corte óptimo para otra longitud?', self.console):
                self.print_algorithm_menu(algorithm)
                print_arr(arr, title='Precios', cols_name='Longitud', rows_name='Precio')
                self.execute_cut_rod(arr, prices, cuts)
            else:
                break

    def execute_cut_rod(self, arr: List, prices: List, cuts: List):
        n = get_int('Ingrese la longitud de la cual se obtendrá el corte óptimo', cota_inf=1, cota_sup=len(arr) - 1)
        price, optimal_cut = build_cut_rod_solution(arr, n, prices, cuts)
        print_arr(optimal_cut, title='Corte óptimo', rows_name='Longitud', cols_name='Número de corte', i=1)
        self.console.print(f'El precio óptimo para una longitud de {n} es: {price}', style='cyan')
