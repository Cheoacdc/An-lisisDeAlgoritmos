from rich.console import Console
from rich.markdown import Markdown

from menus.ordenacion import MenuOrdenacion
from menus.menu import Menu

import utils.console_testing

from utils.helpers import wait_enter
from utils. input_helpers import get_int, confirmation


class MainMenu(Menu):
    def __init__(self):
        super(MainMenu, self).__init__()
        self.options = {
            '1': MenuOrdenacion,
            '2': print,
            '3': print
        }

    def start(self) -> None:
        self.print_md_file('portada')
        while True:
            self.print_md_file('main_menu')
            wait_enter(self.console)
            self.console.print('Para salir en del menú en el que se encuentre, presione "q"', justify='center')
            opc = get_int('¿Qué tipo de algoritmo desea utilizar? (1, 2 o 3)', 1, 3)
            if opc is None:
                if confirmation('Está por salir del programa, ¿desea continuar?', self.console):
                    break
                else:
                    continue
            else:
                self.options[str(opc)](self.console).start()
