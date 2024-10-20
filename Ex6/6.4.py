#4. Fes un programa que demane a l’usuari un nom de directori del sistema
# d’arxius local i mostre el seu contingut. Si passem un directori inexistent mostrarà un
# missatge i en demanarà un altre. Per implementar-ho fes 2 funcions diferents, però semblants,
# una que use la llibreria os i l’altra la pathlib.
import os
from pathlib import Path

def mostrar_contingut_os():
    while True:
        nom_directori = input("Introdueix el nom del directori (complet): ")
        if os.path.isdir(nom_directori):  # Comprovem si el directori existeix
            print("Contingut del directori",nom_directori,":")
            for i in os.listdir(nom_directori):  # Obtenim els elements del directori
                print("-", i)
            break  # Sortim del bucle si el directori és vàlid
        else:
            print("Error: El directori no existeix. Torna-ho a intentar.")

def mostrar_contingut_pathlib():
    while True:
        nom_directori = input("Introdueix el nom del directori (complet): ")
        path = Path(nom_directori)  # Creem un objecte Path
        print(path)
        if path.is_dir():  # Comprovem si el directori existeix
            print("Contingut del directori",nom_directori,":")
            for i in path.iterdir():  # Iterem pels elements del directori
                print("-", i.name)
            break  # Sortim del bucle si el directori és vàlid
        else:
         print("Error: El directori no existeix. Torna-ho a intentar.")
            
print("Usant la llibreria os:")
mostrar_contingut_os()
print("\nUsant la llibreria pathlib:")
mostrar_contingut_pathlib()