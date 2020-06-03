def carton():
    cartonConCeldas = (
        (3,0,22,0,41,52,0,0,89),
        (7,12,0,38,0,57,0,73,0),
        (0,18,25,0,44,0,64,76,0)
    )
    return cartonConCeldas

# cuenta cuantas celdas ocupadas hay
def contar_celdas_ocupadas(mi_carton):
    contador = 0
    for fila in mi_carton:
        for celda in fila:
            if celda != 0:
                contador += 1
    return contador

# retorna true si no hay 3 o mas celdas vacias consecutivas, False en caso contrario
def no_mas_de_3_celdas_vacias(mi_carton):
    for i in range(7):
        for j in range(3):
            if mi_carton[j][i] == 0 and mi_carton[j][i+1] == 0 and mi_carton[j][i+2] == 0:
                return False
    return True

# retorna true si no hay columnas vacias, False en caso contrario
def columnas_ocupadas(mi_carton):
    contador = 0
    for i in range(9):
        for j in range(3):
            if mi_carton[j][i] == 0:
                contador += 1
        if contador == 3:
            return False
        contador = 0
    return True

# retorna true si no hay filas vacias, False en caso contrario
def filas_ocupadas(mi_carton):
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
            if(celda >= 0 and celda <= 0):
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
