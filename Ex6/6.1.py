#1 Escriu un programa que utilitze les següents dos funcions:

#una per obrir un arxiu, dins la qual ens té que demanar el seu nom, informant en un missatge d’error si no es pot obrir (no existix) i en este cas ens el torne a demanar,
#una altra, on passat per paràmetre el nom de l’arxiu introduït abans, ens digue el número de línies que conté.

def obrir_arxiu():
   while True:
       nom_arxiu = input("Introdueix el nom de l'arxiu (amb l'extensió): ") #Demana el nom de l'arxiu
       try:
           arxiu = open(nom_arxiu, 'r')  # Intentem obrir l'arxiu en mode lectura
           return arxiu  # Retornem l'objecte arxiu si s'obre correctament
       except FileNotFoundError:  # Captura l'error si l'arxiu no existeix
           print("Error: No s'ha pogut obrir l'arxiu. Torna-ho a intentar.")

def comptar_linies(arxiu):
   linies=0
   for i in arxiu: #for de les línies
       linies+=1
   return linies

arxiu_obert = obrir_arxiu()  # Obtenim l'arxiu
num_linies = comptar_linies(arxiu_obert)  # Comptem les línies de l'arxiu
arxiu_obert.close()  # Tanquem l'arxiu

print("L'arxiu conté",num_linies,"línies.")