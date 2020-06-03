from src import bingo
mi_carton = bingo.carton()

def test_fila_menor_derecha():
    assert bingo.fila_menor_derecha(mi_carton)

    