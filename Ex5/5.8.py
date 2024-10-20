#8 Realitzar una altra funció que inverteix la llista, però en lloc de tornar una de nova,
# modifique la llista donada per invertir-la, sense usar llistes auxiliars.

def modificarLlista(llista):
   return llista[::-1] #Retorno la llista invertida utiltizant [::-1]

print(modificarLlista(llista= [ 'Digues', 'bon', 'dia', 'al', 'papa']))
