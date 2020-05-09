def carton():
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