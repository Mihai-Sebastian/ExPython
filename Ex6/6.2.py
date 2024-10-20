
#2 Crea un programa que demane a l’usuari que ens digue el nom d’un arxiu a crear i un text per incloure a l’arxiu.
# El text a introduir ha de finalitzar quan l’usuari escrigue ‘fi’. Per implementar-lo heu d’usar dos funcions:
#Per demanar el nom de l’arxiu modifiqueu la de l’exercici anterior,
#La segona rebrà com a paràmegtre el nom de l’arxiu i l’omplirà de text.

def obrir_arxiu_nou():
    while True:
        nom_arxiu = input("Introdueix el nom de l'arxiu (amb l'extensió): ")  # Demana el nom de l'arxiu
        try:
            # Intentem obrir l'arxiu en mode lectura
            arxiu = open(nom_arxiu, 'r')
            arxiu.close()  # Tanquem l'arxiu perquè només volíem comprovar si existia
            print("Error: L'arxiu ja existeix. Introdueix un nom nou.")
        except FileNotFoundError:
            # Si l'arxiu no existeix, sortim del bucle
            return nom_arxiu  # Retornem el nom de l'arxiu per crear-lo


def omplir_arxiu(nom_arxiu):
    with open(nom_arxiu, 'w') as arxiu:  # Obrim l'arxiu en mode escriptura
        while True:
            text = input("Introdueix el text a afegir a l'arxiu (escriu 'fi' per finalitzar): ")
            if text.lower() == "fi":  # Si l'input es "fi" surt del bucle
                break
            arxiu.write(text + "\n")  # Si el text és diferent a "fi" escriurà a l'arxiu amb un salt de línea \n

nom_arxiu = obrir_arxiu_nou() #Agafar el nom de l'arxiu
omplir_arxiu(nom_arxiu)  # Omplim l'arxiu amb el text de l'usuari

print("L'arxiu",nom_arxiu,"ha estat creat i omplert correctament.")