import glob
import os
def recorrerDirectori():
    while True:
        ruta = input("Introdueix el nom del directori (complet): ")
        if os.path.isdir(ruta):
            buscar=input("Vols buscar un arxiu, per expressió regular o veure tot el contingut? arxiu/regex/tot ")
            if buscar == "arxiu":
                arxiu=input("Introdueix el nombre del arxiu: ")
                if arxiu in os.listdir(ruta):
                    print(f"L'arxiu existeix en la ruta indicada")
                    break
            elif buscar == "regex":
                patro=input("Introdueix el patro (regex): ")
                for arxiu in glob.glob(ruta+"/"+patro):
                    print(arxiu)
                break
            elif buscar == "tot":
                for root, dir, files in os.walk(ruta):
                    path=root.split(os.sep)
                    for file in files:
                        print('---', file)
                break
            else:
                print("Has d'indicar arxiu/regex/tot")

        else:
            print("Error: El directori no existeix. Torna-ho a intentar.")
recorrerDirectori()