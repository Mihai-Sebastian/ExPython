# 1. Funció per obrir l'arxiu

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

# 3. Funció per comptar les línies i la longitud de cadascuna
def comptar_linies_i_llargades(nom_arxiu):
    try:
        arxiu = open(nom_arxiu, 'r')  # Obrim l'arxiu en mode lectura
        linies = arxiu.readlines()  # Llegim totes les línies
        print("Total de línies:", len(linies))  # Comptem el nombre total de línies

        for i in range(len(linies)):  # Iterem sobre l'índex de les línies
            linia = linies[i]  # Obtenim cada línia
            print("Línia", i + 1, ":", len(linia)-1, "caràcters")  # Comptem els caràcters

        arxiu.close()  # Tanquem l'arxiu
    except FileNotFoundError:
        print("Error: No es pot obrir l'arxiu", nom_arxiu)


# 1. Crear un nou arxiu i omplir-lo
nom_arxiu = obrir_arxiu_nou() #Agafar el nom de l'arxiu
omplir_arxiu(nom_arxiu)  # Omplim l'arxiu amb el text de l'usuari

# 2. Comptar el número de línies i la longitud de cadascuna
comptar_linies_i_llargades(nom_arxiu)  # Comptem les línies i la longitud
