from src import bingo
mi_carton = bingo.carton_valido()

def test_fila_menor_derecha():
    assert bingo.fila_menor_derecha(mi_carton)

    