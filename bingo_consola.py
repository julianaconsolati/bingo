from src.bingo import carton_valido

print("Tu carton de bingo es:")
carton = carton_valido()
for fila in carton:
    print(*fila, sep = "   ")
