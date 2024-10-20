#2.2. Reescriu el programa del salari usant try i except, de manera que el programa sigue
# capaç de gestionar entrades no numèriques en elegància, mostrant un missatge
# i sortint del programa. A continuació es mostren dos execucions del programa:

try: #Farà el que s'indica a continuació:
    hores=int(input("Introduix les Hores: "))
    tarifa=float(input("Introduix la tarifa per hora: "))
    if hores > 40:
        hores_extra=hores-40 #Resto les hores - 40 per deixar una variable sols amb les hores extra
        hores-=hores_extra #actualitzo les hores normals restant les hores extra
        print("Salari:",round((hores*tarifa)+(hores_extra*tarifa*1.5),2)) #Faig el càlcul multiplicant les hores per tarifa i les hores extra també les multiplico 1.5
    else:
        print("Salari:", round(hores*tarifa,2)) #Si no són més de 40 hores fa la multiplicació normal
except: #En cas d'error sortirà un missatge:
    print("Error, per favor introduix un número")
