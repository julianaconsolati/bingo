from src import bingo
mi_carton = bingo.carton()

def test_sin_numeros_repetidos():
    assert bingo.sin_numeros_repetidos(mi_carton)