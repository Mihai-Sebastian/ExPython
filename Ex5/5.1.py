#1 Escriu una funció anomenada retalla, que prengue una llista, la modifique eliminant els elements
# primer i últim, i retorne None. Mostra què ha passat en la llista paràmetre després de la crida
# a la funció per saber si s’ha modificat o no.

def retalla(llista):
    if len(llista) > 2: #Si la llista té més de 2 números entra al if
        del llista[0]    #elimina la posició 0
        del llista[-1]  #Elimina la última posició [-1]
    elif len(llista) == 2: #Si la llista sols té 2 números elimina tota la llista
        llista.clear() 
    else:  
        print("La llista no té suficients números per retallar.") 
    return None

llista = [1, 2, 3, 4, 5] #llista
print("Abans de retallar:", llista)
retalla(llista) 
print("Després de retallar:", llista) #Sense el return la llista s'ha modificat igual.


