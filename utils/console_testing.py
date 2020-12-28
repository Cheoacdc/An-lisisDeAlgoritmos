import time
import timeit

from rich.progress import Progress


import_module = 'from ordenacion.insertion_sort import insertion_sort'
secs = timeit.timeit('insertion_sort([1,2,3,3,1,2,4,1,2,2,4,4,4,2,2,3,1,2,3,2])', setup=import_module, number=100)
print(secs)
print(secs*1000)
with Progress() as progress:

    task1 = progress.add_task("[red]Ordenando...", total=secs)
    task2 = progress.add_task("[green]Processing...", total=secs)
    task3 = progress.add_task("[cyan]Cooking...", total=secs)

    while not progress.finished:
        progress.update(task1, advance=secs/100)
        progress.update(task2, advance=0.3)
        progress.update(task3, advance=0.9)
        time.sleep(0.01)
