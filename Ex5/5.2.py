#2. Escriu una funció anomenada centre, que prengue una llista i retorne una altra que
# contingue tots els elements de l'original, menys el primer i l'últim.
def centre(llista):
   if len(llista) > 2:  # Comprova que hi ha prou números per retornar el centre
       return llista[1:-1]  # Retorna la llista sense el primer i últim element
   else:
       return []  # Retorna una llista buida si té menys de 3 elements

llista = [1, 2, 3, 4, 5]
print("Llista abans:", llista) #Llista abans de modificar
novaLlista=centre(llista)
print("Llista centrada:", novaLlista) #Llista després de modificar
