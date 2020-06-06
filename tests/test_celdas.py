from src import bingo
mi_carton = bingo.carton_valido()

# testea que el carton tenga 15 celdas ocupadas o menos
def test_menos_de_15():
    assert bingo.contar_celdas_ocupadas(mi_carton) <= 15
    
# testea que el carton tenga 15 celdas ocupadas o mas
def test_mas_de_15():
    assert bingo.contar_celdas_ocupadas(mi_carton) >= 15

# testea que no haya columnas llenas
def test_columnas_llenas():
    assert bingo.columnas_llenas(mi_carton)

# testea que no haya columnas vacias
def test_columnas_vacias():
    assert bingo.columnas_vacias(mi_carton)

# testea que no haya filas vacias
def test_filas_viacias():
    assert bingo.filas_vacias(mi_carton)

# Verifica que no haya filas con 3 celdas vacias consecutivas
def test_no_mas_de_3_celdas_vacias():
    assert bingo.no_mas_de_3_celdas_vacias(mi_carton)

# Verifica que en cada fila haya solo 5 celdas ocupadas
def test_fila_solo_cinco():
    assert bingo.fila_solo_cinco(mi_carton)

# Verifica si el carton tiene 3 y solo 3 columas con solo una celda ocupada
def test_tres_columnas_con_una_celda():
    assert bingo.tres_columnas_con_una_celda(mi_carton)
