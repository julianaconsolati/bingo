from src import bingo
mi_carton = bingo.carton_valido()

def test_fila_mayor_abajo():
    assert bingo.fila_mayor_abajo(mi_carton)