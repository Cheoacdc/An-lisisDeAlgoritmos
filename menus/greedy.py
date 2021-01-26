import time

from greedy.activity_selector import greedy_activity_selector
from greedy.hoffman import build_answer, hoffman

from menus.menu import Menu

from rich.console import Console

from typing import Dict, List

from utils.errors import QuitException
from utils.helpers import print_dict_arr, wait_enter
from utils.input_helpers import confirmation, get_dict_array, get_int


class MenuGreedy(Menu):
    def __init__(self, console: Console):
        super(MenuGreedy, self).__init__(console)
        self.options = {
            '1': {
                'name': 'Códigos de Hoffman',
                'fun': self.execute_hoffman,
                'keys': [
                    {'key': 'letter', 'name': 'letra', 'msg': 'la letra', 'type': 'str'},
                    {'key': 'value', 'name': 'repeticiones', 'msg': 'el número de repeticiones', 'type': 'int'},
                ],
                'description': 'hoffman'
            },
            '2': {
                'name': 'Seleccionador de actividades',
                'fun': self.execute_selector,
                'keys': [
                    {'key': 'start', 'name': 'inicio', 'msg': 'el inicio', 'type': 'int'},
                    {'key': 'end', 'name': 'final', 'msg': 'el final', 'type': 'int'}
                ],
                'description': 'activity_selector'
            }
        }

    def start(self):
        while True:
            self.print_md_file('menu_greedy')
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
                self.console.print('Regresando al menú de algoritmos greedy...', style='bold red')
                time.sleep(1)

    def execute_selector(self, arr: List) -> None:
        sol = greedy_activity_selector(arr)
        print_dict_arr(sol, keys=self.options['2']['keys'], title='La solución es:')

    @classmethod
    def execute_hoffman(cls, arr: List) -> None:
        root = hoffman(arr)
        sol = build_answer(root)
        print_dict_arr(
            sol,
            keys=[{'key': 'letter', 'name': 'letra'}, {'key': 'code', 'name': 'código'}],
            title='La solución es:'
        )

    def execute_algorithm(self, algorithm: Dict):
        if confirmation('¿Desea ver la descripción del algoritmo?', self.console):
            self.print_description(algorithm)
            wait_enter(self.console, 'para proceder al menú del algoritmo')
        self.print_algorithm_menu(algorithm)
        arr = get_dict_array(algorithm['keys'])
        algorithm['fun'](arr)
        wait_enter(self.console, 'para volver al menú de ordenación y búsqueda')
