#2 Escriu un bucle while que comence en l'últim caràcter d’una cadena introduïda per l’usuari
# i faigue el seu recorregut cap enrere fins al primer caràcter de la mateixa,
# mostrant cada lletra en una línea separada.

#Input de la cadena
cadena=str(input("Escriu una cadena: "))
posicio = len(cadena) -1 #longitud de la cadena menys 1 perquè comencem a comptar desde el 0.

#bucle while que s'executarà mentre posició sigue més gran o igual a 0.
while posicio>=0:
   print(cadena[posicio]) #Print de la posició de la cadena, hola = h=0, o=1, l=2, a=3
   posicio-=1 #Restem 1 a posició per a la següent iteració
