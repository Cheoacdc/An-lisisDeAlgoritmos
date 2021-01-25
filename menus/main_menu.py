import time

from menus.graphs_menu import MenuGraphs
from menus.greedy import MenuGreedy
from menus.menu import Menu
from menus.ordenacion import MenuOrdenacion
from menus.prog_din import MenuProgDin

from utils.errors import QuitException
from utils.helpers import wait_enter
from utils.input_helpers import get_int, confirmation


class MainMenu(Menu):
    def __init__(self):
        super(MainMenu, self).__init__()
        self.options = {
            '1': MenuOrdenacion,
            '2': MenuGreedy,
            '3': MenuProgDin,
            '4': MenuGraphs
        }

    def start(self) -> None:
        try:
            self.print_md_file('portada')
            wait_enter(self.console)
            while True:
                self.print_md_file('main_menu')
                total = len(self.options)
                try:
                    opc = get_int(f'¿Qué tipo de algoritmo desea utilizar? (1 a {total})', 1, total)
                    self.options[str(opc)](self.console).start()
                except QuitException:
                    if confirmation('Está por salir del programa, ¿desea continuar?', self.console):
                        break
                    else:
                        continue
        except KeyboardInterrupt:
            pass
        self.console.print('\nSaliendo del programa...', style='bold red')
        time.sleep(0.5)
        self.console.print('Que tenga un buen día :]', style='green')
