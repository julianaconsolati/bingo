from src import bingo
mi_carton = bingo.carton()

def sin_numeros_repeditos():
    assert bingo.sin_numeros_repeditos(mi_carton)