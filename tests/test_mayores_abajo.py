
from src import bingo
mi_carton = bingo.carton()

def test_fila_mayor_abajo():
    assert bingo.fila_mayor_abajo(mi_carton)