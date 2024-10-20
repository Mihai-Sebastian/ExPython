#6. Els germans Pastafullada estan enamorats del seu algorisme.
# Ara volen perfeccionar-lo per saber quins són els números adequats per fer piles triangulars i quadrades indistintament.
# El 36, per exemple, n’és un: Es demana que dissenyeu un algorisme que, donat un número natural, indiqui si és vàlid per fer piles triangulars
# i quadrades indistintament, o només d'un dels dos tipus o de cap.

#Fórmula del numero Triangular
def numeroTriangular(llaunes):
   n=1
   pivot=0
   while True:
       pivot=n*(n+1)/2
       n+=1
       if pivot == llaunes:
           return True
       elif pivot > llaunes:
           return False
#Fórmula amb el mètode babilònic per a saber si el número és quadrat.
#El que fa és dividir fins trobar l'arrel quadrada i si l'arrel quadrada és exacta significa que és un número quadrat.
def metodeBabilonic(llaunes):
   x0=llaunes/2
   tolerancia = 1e-9 #a vegades pot passar que el resultat és 7.999998 en compte de 8, amb la tolerancia s'arregla ja
                     # que deixo un marge de diferència amb el resultat.
   while True:
       x0=0.5*(x0+llaunes/x0)
       if x0*x0 == llaunes and x0.is_integer() == True:
           return True
       elif abs(x0 * x0 - llaunes < tolerancia):
           return False


def main(llaunes):
    numTriangular=numeroTriangular(llaunes)
    mBabilonic=metodeBabilonic(llaunes)
    if numTriangular == True and mBabilonic== True:
        print("El numero es triangular i quadrat")
    elif numTriangular == True and mBabilonic == False:
        print("El numero es sols triangular")
    elif numTriangular==False and mBabilonic==True:
        print("El numero es sols quadrat")
    elif numTriangular == False and mBabilonic== False:
        print("El numero no es cap")

main(llaunes=int(input("Indica el número de llaunes: ")))
