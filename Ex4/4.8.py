#8. Escriu 4 funcions, que donada una cadena i un caràcter:

#a) Inserix el caràcter entre cada lletra de la cadena. Ej: 'separar' i ',' --> 's,e,p,a,r,a,r'
def inserir_caracter_entre_lletres(cadena, caracter):
    return caracter.join(cadena)  # Utilitzo join() per afegir el caràcter entre cada lletra
print(inserir_caracter_entre_lletres('separar', ','))

#b) Substituix tots els espais pel caràcter. Ex: 'el meu fitxer de text.txt' i '_' hauria de tornar 'el_meu_fitxer_de_text.txt'
def substituir_espais(cadena, caracter):
    return cadena.replace(' ', caracter)  # Utilitzo replace() per substituir espais pel caràcter
print(substituir_espais('el meu fitxer de text.txt', '_'))

#c) Substituix tots els dígits a la cadena pel caràcter. Ex: 'la seua clau és: 1540' i 'X' hauria de tornar 'la seua clau és: XXXX'
def substituir_digits(cadena, caracter):
    s=""
    for i in cadena:
        if i.isdigit(): #Si és un dígit afegeixo X a la cadena s.
            s+=str(caracter)
        else: s+=str(i)
    return s
print(substituir_digits('la seua clau és: 1540', 'X'))

#d) Inserix el caràcter cada 3 dígits en la cadena. Ex. '2552552550' i '.' hauria de tornar '255.255.255.0'
def inserir_caracter_cada_tres_digits(cadena, caracter):
    pivot=1
    s=""
    for i in cadena:
        if pivot == 3: #Cada 3 iteracions afegeix el.
            s+=str(i)
            s+=str(caracter)
            pivot=1
        else:
            s+=str(i)
            pivot+=1
    return s
print(inserir_caracter_cada_tres_digits('2552552550', '.'))
