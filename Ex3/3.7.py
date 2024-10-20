# 7. En una pastisseria hi ha m tipus diferents de pastissos. De quantes maneres es poden escollir n pastissos?
# Són les combinacions en repetició d'm elements agafats d'n en n, és a dir:
# Se us demana dissenyar un algorisme que permeti calcular-ho.

#Fórmula per al factorial
def Factorial(n):
   factorial = 1
   for i in range(1, n+1):
       factorial = factorial * i
   return factorial

#Fórmula per a saber les combinacions
def Combinacions(m,n):
   return print(Factorial(m+n-1)/(Factorial(n)*(Factorial(m-1))))

Combinacions(m=int(input("Quants pastissos hi ha? ")),n=int(input("Quants pastissos vols escollir? ")))
