def carton():
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