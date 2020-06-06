from src import bingo
mi_carton = bingo.carton_valido()

def test_celdas_ocupadas_1_a_90():
    assert bingo.celdas_1_a_90(mi_carton)