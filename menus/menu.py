import abc
import os
import time
import timeit

from rich.console import Console
from rich.markdown import Markdown
from rich.progress import Progress

from typing import Dict, List

from utils.helpers import clear_screen, print_arr


class Menu(metaclass=abc.ABCMeta):
    def __init__(self, console: Console = None):
        if console:
            self.console = console
        else:
            self.console = Console()

    def print_md_file(self, filename: str) -> None:
        clear_screen()
        path = os.path.join('md', f'{filename}.md')
        with open(path, encoding="utf-8") as readme:
            markdown = Markdown(readme.read())
        self.console.print(markdown)
        print('\n')

    def print_md(self, string: str) -> None:
        self.console.print(Markdown(string))
        print('\n')

    def print_algorithm_menu(self, algorithm: Dict, arreglo: List = None) -> None:
        clear_screen()
        self.print_md(f'# {algorithm["name"]}')
        if arreglo:
            print_arr(arreglo, 'Arreglo utilizado:', self.console)

    @classmethod
    def progressbar(cls, algorithm: Dict, arr: List, params: List, msg: str):
        statement = f'{algorithm["fun"].__name__}({[n for n in arr]}, *{params})'
        secs = timeit.timeit(statement, setup=algorithm['import'], number=100)
        print(secs)
        secs *= 1000
        print(secs)
        with Progress() as progress:
            task1 = progress.add_task(f"[red]{msg} 100000 veces...", total=secs)

            while not progress.finished:
                progress.update(task1, advance=0.02)
                time.sleep(0.01)

    @abc.abstractmethod
    def start(self):
        pass
