#7 Inversió de llistes. Realitzar una funció que, donada una llista, retorna una nova llista en el mateix contingut
# que l’original però invertida. [ 'Digues', 'bon', 'dia', 'al', 'papa'], haurà de tornar [ 'papa', 'al', 'dia', 'bon', 'Digues'].

def inversioLlistes(llista):
   llista2=[] #Inicialitzo la llista
   for i in llista: #Bucle per recórrer la llista
       llista2.insert(0, i) #Afegeixo cada iteració en la posició 0 de la nova llista
   return llista2 #retorno la nova llista

llista = ['Digues', 'bon', 'dia', 'al', 'papa']
print(llista)
print("Llista invertida:", inversioLlistes(llista))
