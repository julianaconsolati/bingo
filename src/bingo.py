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
