#9 Investigueu i expliqueu què fan els següents mètodes de les llistes, i mostrar exemples del seu ús:
# append
llista = [1, 2, 3]
print(llista)
llista.append(4)  # Afegeix 4 al final de la llista
print(llista)
# # clear
llista = [1, 2, 3]
print(llista)
llista.clear()  # Esborra tots els elements
print(llista)
#copy
llista = [1, 2, 3]
print(llista)
nova_llista = llista.copy()  # Crea una còpia de la llista
print(nova_llista)
#count
llista = [1, 2, 2, 3]
print(llista)
nombre_de_dos = llista.count(2)  # Comptar quantes vegades apareix el número 2
print(nombre_de_dos)
#extend
llista = [1, 2, 3]
print(llista)
llista.extend([4, 5])  # Afegeix els elements [4, 5] a la llista
print(llista)
#index
llista = [1, 2, 3]
print(llista)
index_de_dos = llista.index(2)  # Trobar l'índex (posició) de 2
print(index_de_dos)
#insert
llista = [1, 2, 3]
print(llista)
llista.insert(1, "a")  # Insereix "a" a l'índex (posició) 1
print(llista)
#pop
llista = [1, 2, 3]
print(llista)
darrer_element = llista.pop()  # Elimina l'últim element
print(darrer_element)  # Sortida: 3
print(llista)
#remove
llista = [1, 2, 3, 2]
print(llista)
llista.remove(2)  # Elimina la primera aparició de 2
print(llista)
#reverse
llista = [1, 2, 3]
print(llista)
llista.reverse()  # Inverteix la llista
print(llista)
#sort
llista = [3, 1, 2]
print(llista)
llista.sort()  # Ordena la llista
print(llista)