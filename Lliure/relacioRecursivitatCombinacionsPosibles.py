    # Combinacions de Monedes
    # Exemple:
    # 5 (1 moneda de 5)
    # 2 + 2 + 1 (2 monedes de 2 i 1 de 1)
    # 2 + 1 + 1 + 1 (1 moneda de 2 i 3 de 1)
    # 1 + 1 + 1 + 1 + 1 (5 monedes de 1)

centims = 5
monedes = [1, 2, 5,10,20,50,100,200]

maneres = [0] * (centims + 1)
maneres[0] = 1

for moneda in monedes:

    for i in range(moneda, centims + 1):
        maneres[i] += maneres[i - moneda]

print("Nombre de maneres d'aconseguir", centims, "cèntims utilitzant les monedes:",monedes,)
print("Formes:",maneres[centims])

