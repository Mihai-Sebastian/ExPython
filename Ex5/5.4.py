#4 Escriu una funció que rep dos llistes i retorna el seu producte escalar.
def producte_escalar(llista1, llista2):
    print(llista1, llista2)
    n = min(len(llista1), len(llista2))  # Agafo la llargada de la llista més curta
    suma = 0  # Inicialitzem la suma
    try:
        for i in range(n):
            suma += llista1[i] * llista2[i]  # Sumem a suma el resultat de llista[n] * llista [n]
        return suma
    except TypeError:
        return None  # Retornem None en cas d'error

print(producte_escalar([4,5,6], [1,2,3]))
