
# An-lisisDeAlgoritmos
Proyecto para la materia análisis de algoritmos, del séptimo semestre de la carrera de MAC, cursada en la FES Acatlán.

## Proyecto Final Análisis de Algoritmos
### Profesor: Christian Rubio Montiel
### Alumno: Eliseo Aldair Cabrejos Reyes

### Objetivo
El objetivo de este proyecto es tener todos los algoritmos vistos en clase implementados.

#### Bibliografía:
* Cormen, T. H. et al.(2009). Introduction to algorithms (Third ed.). Cambridge, MA: MIT Press.

#### Módulos externos utilizados:
* Numpy: Para el manejo de arreglos y el uso de infinito.
* Rich: Para una mejor presentación en la consola.

## Instrucciones
Para ejecutar el programa, es evidente que respetar la estructura de los directorios es fundamental, ya que de esto depende el funcionamiento correcto del programa.

Para crear un repositorio copia y descargar los archivos, correr el siguiente comando en el directorio deseado.

```zsh
$ git init
$ git remote add origin https://github.com/Cheoacdc/An-lisisDeAlgoritmos.git
$ git fetch origin
$ git merge origin/master
```

### Dependencias
Por otro lado, es indispensable trabajar con un entorno virtual igual al que se utilizó para el desarrollo del programa. Aquí se presentan dos alternativas.

#### Pipenv (recomendado)
Si se cuenta con pipenv, además de que se instalarán las dependencias, se creará automáticamente un entorno virtual en el directorio en el que se ejecute el siguiente comando.
```zsh
$ pipenv install
```

#### Pip
En caso de no contar con pipenv, simplemente con correr el siguiente comando se instalarán las dependencias.
```zsh
$ pip install -r requirements.txt
```
**Nota:** Este comando no creará un entorno virtual, eso será cuestión del usuario. Para garantizar un entorno tal y cómo se requiere, utilizar la alternativa **pipenv**.

## Descripción de los algoritmos.
Durante la ejecución del programa, después de seleccionar un algoritmo se mostrará la opción de ver la descripción del algoritmo. Los archivos de los cuales se muestra la información se encuentran en el directorio **\md**. Si el usuario lo desea, puede visualizarlos en la página de Github o en algún programa que le permita visualizar archivos tipo **.md**. En estos archivos se muestra la descripción del algoritmo, así como el código que se utiliza para su implementación. El código que se muestre puede no ser idéntico al de los archivos, debido a que se removieron elementos intracendentes y que sólo son relevantes para el lenguaje y no el algoritmo, como el *type hinting*.

## Contacto
* Correo electrónico: eliseo.cabrejos99@gmail.com
* Github: Cheocdc
