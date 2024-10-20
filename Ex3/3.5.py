# 5. A la botiga dels germans Pastafullada és tradició presentar les llaunes de conserva apilades triangularment. Per exemple, sis llaunes es posen com:
# Els germans tenen grans problemes per fer les comandes de llaunes. Fixeu-vos que no tot número de llaunes pot apilar-se triangularment,
# per exemple 8. Es demana que dissenyeu un algorisme que, donat un número natural, determini si representa un número adequat per muntar piles triangulars.

# Forma 2:
def numeroTriangular(llaunes):
   n=0
   for i in range(llaunes):
       #Per a saber si és un número triangular faig un bucle del rang de les llaunes i després sumo
       # n + i+1, exemple: 6 llaunes: 0+1 = 1, 1+2 = 3, 3+3=6, com el resultat és 6 és un número triangular
       #Si la suma és més gran que les llaunes indicades significa que no és un número triangular.
       n+=i+1
       if n == llaunes:
           print("Es triangular")
           break
       elif n > llaunes:
           print("No es triangular")
           break

# numeroTriangular(llaunes=int(input("Indica el número de llaunes: ")))
numeroTriangular(llaunes=int(input("Indica el número de llaunes: ")))

