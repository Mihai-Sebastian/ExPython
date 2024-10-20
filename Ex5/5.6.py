#6 Donada una llista de números enters i un enter k, escriu una funció que:
# retorne tres llistes, una amb els menors, una altra amb els majors i una altra en els iguals a k.

def numeros(llista,k):
   majors=[] #Inicialitzo les 3 llistes
   menors=[]
   iguals=[]

   for num in llista: #Bucle per recórrer cada número de la llista
       if num < k:
           menors.append(num) #Si és més petit que el número indicat s'afegeix a la llista menors
       elif num > k:
           majors.append(num) #Si es més gran que el número indicat s'afegeix a la llista majors
       else:
           iguals.append(num) #Si es igual que el número indicat s'afegeix a la llista iguals
   return menors, iguals, majors #retorna les 3 llistes

llista = [1,2,3,4,5,6,7,8,9,10,11,12,1,3,4,5,1,6,1,7]
k=5
print("Llista:",llista,"\nK:", k)
menors, iguals, majors = numeros(llista, k)
print("Menors que", k, ":", menors)
print("Iguals a", k, ":", iguals)
print("Majors que", k, ":", majors)
