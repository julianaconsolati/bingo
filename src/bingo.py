import random
import math

"""
def carton():
    cartonConCeldas = (
        (3,0,22,0,41,52,0,0,89),
        (7,12,0,38,0,57,0,73,0),
        (0,18,25,0,44,0,64,76,0)
    )
    return cartonConCeldas
"""

# cuenta cuantas celdas ocupadas hay
def contar_celdas_ocupadas(mi_carton):
    contador = 0
    for fila in mi_carton:
        for celda in fila:
            if celda != 0:
                contador += 1
    return contador

# reotrna true si el carton tiene 3 y solo 3 columas con solo una celda ocupada, false en caso contrario
def tres_columnas_con_una_celda(mi_carton):
    aux = 0
    for i in range(9):
        contador = 0
        for j in range(3):
            if mi_carton[j][i] != 0:
                contador += 1
        if contador == 1:
            aux += 1
    if aux != 3:
        return False
    return True

# retorna true si cada fila tiene solo 5 celdas ocupadas
def fila_solo_cinco(mi_carton):
    for fila in mi_carton:
        contador = 0
        for celda in fila:
            if celda != 0:
                contador += 1
        if contador != 5:
            return False
    return True

# retorna true si no hay 3 o mas celdas vacias consecutivas, false en caso contrario
def no_mas_de_3_celdas_vacias(mi_carton):
    for i in range(7):
        for j in range(3):
            if mi_carton[j][i] == 0 and mi_carton[j][i+1] == 0 and mi_carton[j][i+2] == 0:
                return False
    return True

# retorna true si no hay columnas vacias, false en caso contrario
def columnas_vacias(mi_carton):
    contador = 0
    for i in range(9):
        for j in range(3):
            if mi_carton[j][i] == 0:
                contador += 1
        if contador == 3:
            return False
        contador = 0
    return True

# retorna true si no hay columnas llenas, False en caso contrario
def columnas_llenas(mi_carton):
    contador = 0
    for i in range(9):
        for j in range(3):
            if mi_carton[j][i] != 0:
                contador += 1
        if contador == 3:
            return False
        contador = 0
    return True

# retorna true si no hay filas vacias, False en caso contrario
def filas_vacias(mi_carton):
    contador = 0
    for i in range(3):
        for j in range(9):
            if mi_carton[i][j] == 0:
                contador += 1
        if contador == 9:
            return False
        contador = 0
    return True

# Retorna True si no hay numeros repetido, False en caso contrario
def sin_numeros_repeditos(mi_carton):
    for fila in mi_carton:
        for celda in fila:
            if celda != 0:
                for fila2 in mi_carton:
                    for celda2 in fila2:
                        if celda == celda2:
                            return False
    return True

# Retorna True si las celdas ocupadas se encuentran entre 1 y 90, False en caso contrario
def celdas_1_a_90(mi_carton):
    for fila in mi_carton:
        for celda in fila:
            if(celda >= 0 and celda <= 90):
                return True
    return False

# Retorna True si todos los numeros van de menor a mayor de arriba hacia abajo, False en caso contrario
def fila_mayor_abajo(mi_carton):
    for i in range(8):
        for j in range(3):
            if mi_carton[j][i] > mi_carton[j][i+1] and mi_carton[j][i+1] != 0:
                return False
    return True

# Retorna True si las celdas ocupadas son mayores que la de su izquierda, False en caso contrario
def fila_menor_derecha(mi_carton):
    for i in range(9):
        for j in range(2):
            if mi_carton[j][i] > mi_carton[j+1][i] and mi_carton[j+1][i] != 0:
                return False
    return True




# Genera un carton (valido o no)
def nuevo_carton():
    contador = 0

    carton = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
    ]
    numerosCarton = 0

    while numerosCarton < 15:
        contador += 1
        if contador == 50 :
            return nuevo_carton()
        numero = random.randint(1, 90)

        columna = math.floor(numero / 10)
        if columna == 9:
            columna = 8
        huecos = 0
        for i in range(3):
            if carton[i][columna] == 0:
                huecos += 1
            if carton[i][columna] == numero:
                huecos = 0
                break
        if(huecos < 2):
            continue

        fila = 0
        for j in range(3):
            huecos = 0
            for i in range(9):
                if carton[fila][i] == 0:
                    huecos += 1
            if huecos < 5 or carton[fila][columna] != 0:
                fila += 1
            else:
                break
        if fila == 3:
            continue

        carton[fila][columna] = numero
        numerosCarton += 1
        contador = 0

    for x in range(9):
        huecos = 0
        for y in range(3):
            if carton[y][x] == 0:
                huecos += 1
        if huecos == 3:
            return nuevo_carton()
    return carton

def imprimirCarton(carton) :
    for fila in carton:
        for celda in fila:
            print(celda, end='  ')
        print()

def main():
    imprimirCarton(nuevo_carton())

if __name__=="__main__":
    main()
    
""" esto pa despues
while True:
    carton = nuevo_carton()
    if(contar_celdas_ocupadas(carton) == 15
    and fila_solo_cinco(carton)
    and columnas_vacias(carton)
    and filas_vacias(carton)
    and columnas_llenas(carton)
    and celdas_1_a_90(carton)
    and fila_menor_derecha(carton)
    and fila_mayor_abajo(carton)
    and sin_numeros_repeditos(carton)
    and tres_columnas_con_una_celda(carton)
    and no_mas_de_3_celdas_vacias(carton)):
        break
"""