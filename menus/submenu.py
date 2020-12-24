import abc

from menus.menu import Menu

from rich.console import Console


class Submenu(Menu, metaclass=abc.ABCMeta):
    def __init__(self, console: Console):
        super(Submenu, self).__init__(console)

