#6. Useu el mètode walk() per recórrer el contingut d’un
# directori existent, indicat per l’usuari. Feu que hi haigue l’opció de
# vore tot el contingut del directori, o de parar si/quan es trobe cert directori/arxiu indicat per l’usuari.
import os
def recorrerDirectori():
    while True:
        ruta = input("Introdueix el nom del directori (complet): ")
        if os.path.isdir(ruta):
            buscar=input("Vols buscar un arxiu o veure tot el contingut? arxiu/tot ")
            if buscar == "arxiu":
                arxiu=input("Introdueix el nombre del arxiu: ")
                if arxiu in os.listdir(ruta):
                    print(f"L'arxiu existeix en la ruta indicada")
                    break

            elif buscar == "tot":
                for root, dir, files in os.walk(ruta):
                    path=root.split(os.sep)
                    for file in files:
                        print('---', file)
                break
        else:
            print("Error: El directori no existeix. Torna-ho a intentar.")
recorrerDirectori()