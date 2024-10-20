#5. Amplieu l’exercici anterior, fent que a més es demane si volem
# llistar arxius, directoris, o ambdós. A la llista mostreu la màxima
# informació possible dels elements a mostrar (useu el mètode stat(),
# i mireu/imprimiu el que conté, mostrant les dates de forma amigable, i indicant en cada cas quina informació mostra).
import os
from pathlib import Path

# Funció que utilitza os
def mostrar_contingut_os():
    while True:
        nom_directori = input("Introdueix el nom del directori (complet): ")
        if os.path.isdir(nom_directori):  # Comprovem si el directori existeix
            opcio = input("Vols llistar arxius, directoris o les dos? (a/d/ambdos): ").lower()
            print("Contingut del directori",nom_directori,":")
            for element in os.listdir(nom_directori):  # Obtenim els elements del directori
                ruta_element = os.path.join(nom_directori, element)  # Ruta completa de l'element
                if opcio == 'a' and os.path.isfile(ruta_element):  # Si només volem arxius
                    mostrar_informacio(ruta_element)
                elif opcio == 'd' and os.path.isdir(ruta_element):  # Si només volem directoris
                    mostrar_informacio(ruta_element)
                elif opcio == 'ambdos':  # Si volem les dos
                    mostrar_informacio(ruta_element)
            break  # Sortim del bucle si el directori és vàlid
        else:
            print("Error: El directori no existeix. Torna-ho a intentar.")

# Funció que utilitza pathlib
def mostrar_contingut_pathlib():
    while True:
        nom_directori = input("Introdueix el nom del directori (complet): ")
        path = Path(nom_directori)  # Creem un objecte Path
        if path.is_dir():  # Comprovem si el directori existeix
            opcio = input("Vols llistar arxius, directoris o les dos? (a/d/ambdos): ").lower()
            print("Contingut del directori",nom_directori,":")
            for element in path.iterdir():  # Iterem pels elements del directori
                if opcio == 'a' and element.is_file():  # Si només volem arxius
                    mostrar_informacio_pathlib(element)
                elif opcio == 'd' and element.is_dir():  # Si només volem directoris
                    mostrar_informacio_pathlib(element)
                elif opcio == 'ambdos':  # Si volem les dos
                    mostrar_informacio_pathlib(element)
            break  # Sortim del bucle si el directori és vàlid
        else:
            print("Error: El directori no existeix. Torna-ho a intentar.")

# Funció per mostrar la informació de l'element amb os
def mostrar_informacio(ruta_element):
    info = os.stat(ruta_element)  # Obtenim la informació de l'element
    if os.path.isfile(ruta_element):
        tipus="Arxiu"
    else:
        tipus="Directori"
    print("\nTipus:",tipus)
    print("NOM:", os.path.basename(ruta_element))
    print("SIZE:",info.st_size,"bytes")

# Funció per mostrar la informació de l'element amb pathlib
def mostrar_informacio_pathlib(element):
    info = element.stat()  # Obtenim la informació de l'element
    if element.is_file():
        tipus = "Arxiu"
    else:
        tipus = "Directori"
    print("\nTipus:",tipus)
    print("NOM:",element.name)
    print("SIZE:",info.st_size,"bytes")

print("Usant la llibreria os:")
mostrar_contingut_os()

print("\nUsant la llibreria pathlib:")
mostrar_contingut_pathlib()
