# 2.1. Reescriu el programa del càlcul del salari per donar-li a l'empleat 1.5 vegades
# la tarifa horària per a totes les hores treballades que excedeixin de 40.
hores=int(input("Introduix les Hores: "))
tarifa=float(input("Introduix la tarifa per hora: "))
if hores > 40: #Entra al if quan hores sigui mes gran que 40
    hores_extra=hores-40 #Variable per a guardar les hores extra
    hores-=hores_extra #resta de les hores extra per a que hores sols tingui les normals i no les extra
    print("Salari:",round((hores*tarifa)+(hores_extra*tarifa*1.5),2)) #resultat
else:
    print("Salari:", round(hores*tarifa,2)) #Si no hi ha mes de 40 hores se paga tota la tarifa igual