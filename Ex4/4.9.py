#9. Escriu 4 funcions que, donada una cadena de caràcters:
#a) Retorne només les lletres consonants. Per exemple, si rep 'algoritmes' o 'logaritmes' ha de tornar 'lgrtms'.

def obtenir_consonants(cadena):
    vocals = "aeiouAEIOU"
    return "".join([i for i in cadena if i not in vocals and i.isalpha()])  # Retorna només les consonants

print(obtenir_consonants('algoritmes'))
print(obtenir_consonants('logaritmes'))

#b) Retorne només les lletres vocals. Per exemple, si rep 'sense consonants' ha de tornar 'eeooa'.

def obtenir_vocals(cadena):
    vocals = "aeiouAEIOU"
    return "".join([i for i in cadena if i in vocals])  # Retorna només les vocals
print(obtenir_vocals('sense consonants'))

#c) Reemplace cada vocal per la següent vocal. Per exemple, si rep 'vestuari' ha de tornar 'vistaero'.

def substituir_vocals_seguents(cadena):
    vocals = "aeiouaAEIOUA"
    resultat = []
    for i in cadena:
        if i in vocals:
            index = vocals.index(i)
            resultat.append(vocals[index + 1])  # Substitueix la vocal per la següent
        else:
            resultat.append(i)  # Deixa les consonants i altres caràcters com estan
    return "".join(resultat)
print(substituir_vocals_seguents('vestuari'))

#d) Indique si es tracta d'un palíndrom. Per exemple, 'A flacs ell escalfa' és un palíndrom (es llegix igual d'esquerra a dreta que de dreta a esquerra).

def es_palindrom(cadena):
    #El que faig per a saber si és un palíndrom és invertir la cadena sense espais i comparar si les 2 llistes són iguals.
    frase1 = cadena.replace(" ","")
    if frase1.lower() == frase1[::-1].lower():
        return "és un palíndrom"
    else:
        return "no és un palíndrom"

print(es_palindrom('A flacs ell escalfa'))
