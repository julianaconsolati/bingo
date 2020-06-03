from src import bingo
mi_carton = bingo.carton()

def sin_numeros_repetidos():
    assert bingo.sin_numeros_repetidos(mi_carton)