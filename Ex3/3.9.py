#9. Dissenyeu un algorisme que determine si un número natural és perfecte. Un número natural
# s’anomena perfecte quan és igual a la suma de tots els seus divisors, llevat d’ell mateix.
# Per exemple, 28 és perfecte perquè 28 = 1 + 2 + 4 + 7 + 14.

def numeroNaturalPerfecte(numero):
   llista=[]
   for i in range(numero):
       i+=1
       if numero % i==0 and i != numero: #Afegeixo tots els divisors a una llista menys el mateix número.
           llista.append(i)
   if sum(llista)==numero: #Si la suma dels divisors és igual al número significa que és un número natural perfecte
       return print("Numero Natural Perfecte")
   else:
       return print("Nuermo NO Natural Perfecte")

numeroNaturalPerfecte(numero=int(input("Indica un número: ")))
