[![Build Status](https://travis-ci.com/julianaconsolati/bingo.svg?branch=master)](https://travis-ci.com/julianaconsolati/bingo)
[![Coverage Status](https://coveralls.io/repos/github/julianaconsolati/bingo/badge.svg?branch=master)](https://coveralls.io/github/julianaconsolati/bingo?branch=master)
# Bingo
Código en Python que genera un cartón de bingo.
Escrito para Adaptación Del Ambiente De Trabajo, Instituto Politécnico Superior "Gral. San Martín", 2020.
Juliana Consolati 6to Informática
## Reglas
Se considara un cartón válido al que cumple con las siguientes condiciones:
* Cada carton es una matriz de 3 x 9.
* Los números del carton se encuentran en el rango 1 a 90.
* Cada columna de un carton (contando de izquierda a derecha) contiene numeros que van del 1 al 9, 10 al 19, 20 al 29 ..., 70 al 79 y 80 al 90.
* No hay números repetidos en el carton.
* Cada fila de un carton tiene exactamente 5 celdas ocupadas.
* Cada carton tiene 15 celdas ocupadas.
* Para una misma columna, sus números están ordenados de menor a mayor de arriba hacia abajo.
* No pueden existir columnas vacias.
* No pueden existir columnas con sus tres celdas ocupadas.
* Cada carton debe tener 3 y solo 3 columas con solo una celda ocupada.
* En una fila no existen más de dos celdas vacías consecutivas.
* En una fila no existen más de dos celdas ocupadas consecutivas.

## Uso e Instalación
Para clonar el repositorio:
```
git clone https://github.com/julianaconsolati/bingo.git
```
Instalar los requerimientos:
```
pip install -r requirements.txt
```
Para ejecutar el código, en versión consola:
```
python bingo_consola.py
```
Para ejecutar el código, en versión web:
```
python bingo_lindo.py
```
Generará otro archivo `bingo.html`, ejecutarlo preferentemente con un navegador

Nota: para distribuciones basadas en Debian utilizar `python3`

Para más información sobre cómo instalar o actualizar Python visite https://www.python.org/

## Ejemplo de salida
```
$ python bingo_consola.py

Tu carton de bingo es:
4   0   25   35   0   0   61   73   0
6   13   28   0   0   56   0   0   84
0   16   0   0   49   58   66   0   90

```
