#1. Escriu un programa que llig repetidament números fins que l'usuari introduix "fi".
# Un cop s'hagi introduït "fi", mostra per pantalla el total, la quantitat de números i la mitjana.
# Si l'usuari introduix qualsevol altra cosa que no sigue un número, detecta el seu error fent servir try i except,
# mostra un missatge d'error i passa al número següent.

llista=[]
while(True): #While True per a que entre al bucle
    try:
        #Input del número del usuari
        numero=input("Introduix un número:")
        #Si l'input de l'usuari és fi farà un break per a sortir del bucle
        if numero == "fi":
            break
        else:
            #Si no ho afegirà a la llista
            llista.append(int(numero))
    #En cas d'entrada invàlida:
    except:
        print("Entrada invàlida")
#Utilitzo sum i len per a fer l'operació
print(sum(llista),len(llista),sum(llista)/len(llista))
