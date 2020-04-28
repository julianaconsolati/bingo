from src.bingo import carton

# cuenta cuantas celdas con 1s hay
def contar_celdas_ocupadas():
    mi_carton = carton()
    contador = 0
    for fila in mi_carton:
        for celda in fila:
            contador += celda
    return contador

# testea que el carton tenga 15 celdas ocupadas o menos
def test_menos_de_15():
    assert contar_celdas_ocupadas() <= 15

# testea que el carton tenga 15 celdas ocupadas o mas
def test_mas_de_15():
    assert contar_celdas_ocupadas() >= 15

# testea que el carton tenga al menos una celda ocupada en todas las columnas
def test_columnas_ocupadas():
    mi_carton = carton()
    contador = 0
    for i in range(9):
        for j in range(3):
            if mi_carton[j][i] == 0:
                contador += 1
        if contador == 3:
            assert False
        contador = 0
    assert True

<<<<<<< HEAD
=======
def test_filas_ocupadas():
    mi_carton = carton()
    contador = 0
    for i in range(3):
        for j in range(9):
            if mi_carton[i][j] == 0:
                contador += 1
        if contador == 9:
            assert False
        contador = 0
    assert True
>>>>>>> 3ee65e562219e76152f3cca3b4e684592c4d0564
