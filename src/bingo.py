def carton():
<<<<<<< HEAD
    cartonConCeldas = (
        (3,0,22,0,41,52,0,0,89),
        (7,12,0,38,0,57,0,73,0),
        (0,18,25,0,44,0,64,76,0)
    )
    return cartonConCeldas

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
=======
    carton = (
        (0,0,27,36,0,52,62,0,80),
        (0,11,0,37,41,0,0,75,88),
        (3,12,0,0,48,0,65,76,0)
    )
    return carton

# Retorna True si las celdas ocupadas se encuentran entre 1 y 90, False en caso contrario
def celdas_1_a_90(mi_carton):
    for fila in mi_carton:
        for celda in fila:
            if(celda >= 0 and celda <= 0):
                return True
    return False
>>>>>>> 80f312ff320f77429dc7ee3813c7e242078a5fb8
