#4 Fes un programa en una funció anomenada comptador, que accepte una cadena i una lletra
# com a arguments i compte/retorne el número de vegades que apareix la lletra a la cadena.


def comptadorLletres(cadena,lletra):
   total=0
   for i in cadena: #Iteració lletra per lletra de la cadena
       if i == lletra: #Si i == lletra total sumarà 1
           total+=1
   return print(total)
cadena="banana"
lletra="a"
print("Cadena:",cadena)
print("Lletra:",lletra)
comptadorLletres(cadena,lletra)

