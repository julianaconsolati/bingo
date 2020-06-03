from src import bingo
mi_carton = bingo.carton()

# testea que el carton tenga 15 celdas ocupadas o menos
def test_menos_de_15():
    assert bingo.contar_celdas_ocupadas(mi_carton) <= 15
    
# testea que el carton tenga 15 celdas ocupadas o mas
def test_mas_de_15():
    assert bingo.contar_celdas_ocupadas(mi_carton) >= 15

# testea que no haya columnas vacias
def test_columnas_ocupadas():
    assert bingo.columnas_ocupadas(mi_carton)

# testea que no haya filas vacias
def test_filas_ocupadas():
    assert bingo.filas_ocupadas(mi_carton)