# 10. Dissenyeu un algorisme per determinar si un número natural és primer.
# Un número n > 1 és primer si els seus únics divisors (factors) són 1 i ell mateix.

def numeroNaturalPrimer(numero):
   llista=[]
   for i in range(numero):
       i+=1
       if numero % i==0: #Afegeixo tots els divisors a una llista.
           llista.append(i)
   if len(llista)==2 or llista[0]==1 and len(llista)==1: #Si la llista té una longitud diferent a 2 (número 1 i ell mateix) significa que no és un numero natural primer.
       return print("Numero Natural Primer")
   else:
       return print("Numero NO Natural Primer")

numeroNaturalPrimer(numero=int(input("Indica un número: ")))
