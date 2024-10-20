#2.3. Escriu un programa que sol·liciti una puntuació entre 0.0 i 1.0.
# Si la puntuació està fora d'este rang, mostra un missatge d'error.
# Si la puntuació està entre 0.0 i 1.0, mostra la qualificació usant la taula següent:

try:
    #Input i una comprovació per saber si ha ficat un número més petit que 0 o més gran que 1
    puntuacio=float(input("Introduix puntuació:"))
    if puntuacio < 0.0 or puntuacio > 1.0:
        print("puntuació incorrecta")
    else:
        #condicionals per a saber la nota
        if puntuacio >= 0.9:
            print("excel·lent")
        elif puntuacio >= 0.8:
            print("notable")
        elif puntuacio >= 0.7:
            print("bé")
        elif puntuacio >= 0.6:
            print("suficient")
        elif puntuacio < 0.6:
            print("insuficient")
#Si fica alguna cosa que no sigue un número salta el missatge:
except:
    print("puntuació incorrecta")


