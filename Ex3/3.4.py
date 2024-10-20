#4. Dissenyeu un algorisme que determini si un número natural és de l’apocalipsi.
# Un número és de l’apocalipsi si conté tres dígits consecutius de la forma 666.
def numApocalipsis(num):
    #Utilitzo in per a saber si 666 està dins de num.
   if "666" in str(num):
       return print("Apocalipsis")
   else: return print("No Apocalipsis")
numApocalipsis(num=input("Indica un numero: "))

