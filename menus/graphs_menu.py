import time

from menus.menu import Menu

from graphs.breadth_first_search import bfs_dict
from graphs.depth_first_search import dfs_dict
from graphs.dijkstra import bellman_ford, dijkstra
from graphs.ford import ford_fulkerson
from graphs.kruskal import kruskal
from graphs.topological_sort import topological_sort_dict


from rich.console import Console

from typing import Dict, List

from utils.errors import QuitException
from utils.helpers import print_dict_arr, print_dict_graph, wait_enter
from utils.input_helpers import confirmation, get_int, get_str


class MenuGraphs(Menu):
    def __init__(self, console: Console):
        super(MenuGraphs, self).__init__(console)
        self.graph = {}
        self.last = ''
        self.options = {
            '1': {
                'name': 'Breadth First Search',
                'fun': self.bfs_menu,
                'keys': [
                    {'key': 'distancia', 'name': 'nodos de distancia'},
                    {'key': 'predecesor', 'name': 'predecesor'}
                ]
            },
            '2': {
                'name': 'Depth First Search',
                'fun': self.execute_dfs,
                'keys': [
                    {'key': 'i', 'name': 'tiempo al entrar'},
                    {'key': 'f', 'name': 'tiempo al salir'},
                    {'key': 'predecesor', 'name': 'predecesor'}

                ]
            },
            '3': {
                'name': 'Topological Sort',
                'fun': self.execute_topological_sort
            },
            '4': {
                'name': 'Dijkstra',
                'fun': self.dijkstra_menu,
                'keys': [
                    {'key': 'distancia', 'name': 'distancia'},
                    {'key': 'predecesor', 'name': 'predecesor'}
                ]
            },
            '5': {
                'name': 'Bellman-Ford',
                'fun': self.bellman_ford_menu,
                'keys': [
                    {'key': 'distancia', 'name': 'distancia'},
                    {'key': 'predecesor', 'name': 'predecesor'}
                ]
            },
            '6': {
                'name': 'Ford-Fulkerson',
                'fun': self.execute_ford,
            },
            '7': {
                'name': 'Kruskal',
                'fun': self.execute_kruskal,
                'keys': [
                    {'key': 'u', 'name': 'u'},
                    {'key': 'v', 'name': 'v'},
                    {'key': 'w', 'name': 'peso'}
                ]
            }
        }

    def start(self):
        while True:
            self.print_md_file('menu_graphs')
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
        self.print_algorithm_menu(algorithm)
        algorithm['fun'](algorithm)
        wait_enter(self.console, 'para volver al menú de ordenación y búsqueda')

    def bfs_menu(self, algorithm: Dict):
        compatible = self.last in ['dfs', 'bfs', 'topological']
        self.set_graph(compatible)
        self.last = 'bfs'
        while True:
            while True:
                node_name = get_str('Ingrese el nodo del cual partir')
                if node_name not in self.graph:
                    self.console.print('Ingrese un nodo que se encuentre dentro del grafo...', style='bold red')
                    self.mostrar_nodos(self.graph)
                    continue
                break
            bfs_dict(self.graph, self.graph[node_name])
            print_dict_graph(
                self.graph, keys=algorithm['keys'],
                title=f'Nodos y sus distancias desde el nodo {node_name}',
                console=self.console
            )
            if confirmation('¿Desea calcular distancias a partir de otro nodo?', self.console):
                self.print_algorithm_menu(algorithm, self.graph, weighted=False)
            else:
                break
        pass

    def execute_dfs(self, algorithm: Dict):
        compatible = self.last in ['dfs', 'bfs', 'topological']
        self.last = 'dfs'
        self.set_graph(compatible)
        dfs_dict(self.graph)
        print_dict_graph(self.graph, algorithm['keys'], title='Al terminar depth first search', console=self.console)

    def execute_topological_sort(self, algorithm: Dict):
        compatible = self.last in ['dfs', 'bfs', 'topological']
        self.set_graph(compatible)
        self.last = 'topological'
        result = topological_sort_dict(self.graph)
        self.console.print('El orden topológico es:', style='bold', justify='center')
        self.console.print(" -> ".join(result), style='bold blue', justify='center')

    def dijkstra_menu(self, algorithm: Dict):
        compatible = self.last == 'dijkstra'
        self.set_graph(compatible, weighted=True)
        self.last = 'dijkstra'
        while True:
            while True:
                node_name = get_str('Ingrese el nodo del cual partir')
                if node_name not in self.graph:
                    self.console.print('Ingrese un nodo que se encuentre dentro del grafo...', style='bold red')
                    self.mostrar_nodos(self.graph)
                    continue
                break
            dijkstra(self.graph, self.graph[node_name])
            print_dict_graph(
                self.graph, keys=algorithm['keys'],
                title=f'Nodos y sus distancias desde el nodo {node_name}',
                console=self.console
            )
            if confirmation('¿Desea calcular distancias a partir de otro nodo?', self.console):
                self.print_algorithm_menu(algorithm, self.graph, weighted=True)
            else:
                break
        pass

    def bellman_ford_menu(self, algorithm: Dict):
        compatible = self.last in ['dijkstra', 'bellman', 'kruskal']
        self.set_graph(compatible, weighted=True, negative=True)
        self.last = 'bellman'
        while True:
            while True:
                node_name = get_str('Ingrese el nodo del cual partir')
                if node_name not in self.graph:
                    self.console.print('Ingrese un nodo que se encuentre dentro del grafo...', style='bold red')
                    self.mostrar_nodos(self.graph)
                    continue
                break
            bellman_ford(self.graph, self.graph[node_name])
            print_dict_graph(
                self.graph, keys=algorithm['keys'],
                title=f'Nodos y sus distancias desde el nodo {node_name}',
                console=self.console
            )
            if confirmation('¿Desea calcular distancias a partir de otro nodo?', self.console):
                self.print_algorithm_menu(algorithm, self.graph, weighted=False)
            else:
                break
        pass

    def execute_ford(self, algorithm: Dict):
        self.graph = self.get_graph(ford=True, weighted=True)
        self.last = 'ford'
        ford_fulkerson(self.graph)
        flujo = 0
        flujos = self.graph['well']['flujos']
        for f in flujos:
            flujo -= flujos[f]
        self.console.print(f'El flujo máximo de la gráfica es: {flujo}', style='bold blue')
        pass

    def execute_kruskal(self, algorithm: Dict):
        compatible = self.last in ['dijkstra', 'bellman', 'kruskal']
        self.set_graph(compatible, weighted=True, negative=True)
        self.last = 'kruskal'
        sol = kruskal(self.graph)
        print_dict_arr(
            sol,
            keys=algorithm['keys'],
            title='Aristas pertenecientes al árbol de expansión mínima (u,v)',
            console=self.console
        )

    def set_graph(self, compatible: bool = False, ford: bool = False, weighted: bool = False, negative: bool = False):
        if self.graph and compatible:
            self.console.print("Ya se había ingresado una gráfica:", justify='center')
            self.print_graph(self.graph)
            if confirmation('¿desea seguir utilizando la misma?'):
                return
        self.graph = self.get_graph(ford, weighted, negative)

    def get_graph(self, ford: bool = False, weighted: bool = False, negative: bool = False) -> Dict or None:
        cota_inf = None if negative else 0
        vecinos = 'vecinos' if not ford else 'capacidades'
        while True:
            n = get_int('¿Cuántos nodos tiene el grafo?', cota_inf=1)
            if confirmation(f'Se creará un grafo con {n} nodos, ¿desea continuar?'):
                break
        if n is None:
            return None
        while True:
            graph = {}
            print('')
            for i in range(0, n):
                while True:
                    if ford:
                        if i == 0:
                            print('El primer y último nodo serán reservados con el nombre de source y well, respectivamente')
                            node_name = 'source'
                        elif i == n - 1:
                            node_name = 'well'
                        else:
                            input_str = f'Ingrese el nombre del nodo #{i + 1}'
                            node_name = get_str(input_str)
                    else:
                        input_str = f'Ingrese el nombre del nodo #{i + 1}'
                        node_name = get_str(input_str)
                    if node_name in graph:
                        self.console.print('Ya se asignó un nodo con ese nombre, intente de nuevo...', style='bold red')
                        continue
                    if weighted:
                        node = {'name': node_name, vecinos: {}, 'flujos': {}} if ford else {'name': node_name, vecinos: {}}
                    else:
                        node = {'name': node_name, vecinos: []}
                    graph[node_name] = node
                    break
            self.console.print('El grafo tiene los siguientes nodos: ', justify='center')
            nodes = ', '.join([n for n in graph])
            self.console.print(nodes, style='bold blue', justify='center')
            if confirmation():
                break
        while True:
            for node in graph:
                if node == 'well':
                    print('El nodo "well" no puede tener exnodos.')
                    n = 0
                else:
                    while True:
                        n = get_int(f'\n¿Cuántos exnodos tiene el nodo {node}?', cota_inf=0, cota_sup=len(graph) - 1)
                        if confirmation(f'Se asignarán {n} exnodos al nodo {node}, ¿desea continuar?'):
                            break
                for i in range(n):
                    while True:
                        vecino = get_str(f'\nIngrese el nombre del exnodo #{i + 1}')
                        if vecino not in graph:
                            self.console.print('**Debe ingresar el nombre de algún nodo perteneciente al grafo**\n', style='bold red')
                            self.mostrar_nodos(graph, [node, *graph[node][vecinos]])
                            continue
                        if vecino == node:
                            self.console.print('**No se permiten loops**', style='bold red')
                            self.mostrar_nodos(graph, [node, *graph[node][vecinos]])
                            continue
                        if vecino in graph[node][vecinos]:
                            print(f'**{vecino} ya se había ingresado**')
                            self.mostrar_nodos(graph, [node, *graph[node][vecinos]])
                            continue
                        break
                    if weighted:
                        while True:
                            val = get_int(f'¿Cuál es el peso de "{node}" a "{vecino}"?', cota_inf=cota_inf)
                            if confirmation(f'Se asignará el peso de "{node}" a "{vecino}" igual a {val}, ¿desea continuar?'):
                                break
                        graph[node][vecinos][vecino] = val
                    else:
                        graph[node][vecinos].append(vecino)
            self.print_graph(graph, vecinos, weighted)
            if confirmation():
                break
        return graph

    def get_shortest_path(self, node: str):
        current_node = node
        path = []
        while True:
            predecesor = self.graph[current_node]['predecesor']
            newpath = [current_node]
            newpath.extend(path)
            path = newpath
            if predecesor is None:
                break
            current_node = predecesor
        return path

    @classmethod
    def mostrar_nodos(cls, graph: Dict, no_disponibles: List = None):
        if no_disponibles is None:
            no_disponibles = []
        string = 'Los nodos posibles son '
        for n in graph:
            if n not in no_disponibles:
                string += f'{n}, '
        string = string[:-2]
        string += '.'
        print(string)
