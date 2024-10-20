#8. Es demana que dissenyeu un algorisme que simule el llançament simultani d’un dau i d’una moneda 100 vegades,
# i informe de quantes vegades ha sortit simultàniament un número senar en el dau i cara a la moneda.

import random
def dauMoneda(llancament):
   contador=0
   for i in range(llancament):
       dau=random.randint(1,6) #EL dau tindrà un número random del 1 al 6.
       moneda=random.choice(["cara","creu"]) #La moneda tindrà cara o creu de forma aleatoria.
       if dau % 2 != 0 and moneda == "cara": #Condicional per si és impar i cara.
           contador+=1 #Suma 1 al contador per cada vegada que es compleix la condició
   return print(contador)
dauMoneda(llancament=int(input("Quantes vegades vols llançar el dau? ")))
