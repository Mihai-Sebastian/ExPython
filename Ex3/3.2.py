# 2.  Escriu un altre programa que demane una llista de números com l'anterior i al final mostre
# per pantalla el màxim i mínim dels números, en comptes de la mitjana.
# Nota: Per resoldre'l useu el valor None tal i com es mostra a l'exemple dels apunts

llista = [1,4,5,6,7,12,5,2,6,-1]
major=None
menor = None
#For per récorrer la llista
for i in llista:
    #Si no te cap valor (None) o si es mes gran que la variable major entra al if
   if major is None or i > major:
       major = i #modifica el valor de la variable major amb la iteració actual
    #Fa el mateix però ara amb el número més petit
   if menor is None or i < menor:
       menor=i
print("Major:",major)
print("Menor:",menor)
