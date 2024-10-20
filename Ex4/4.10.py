#10. Escriure 2 funcions que, donades dues cadenes de caràcters:

#a) Indique si la segona cadena és una subcadena de la primera. Per exemple, 'cadena' és una subcadena de 'subcadena'.
def es_subcadena(cadena1, cadena2):
    print("Subcadena:",cadena1)
    print("Cadena:",cadena2)
    return cadena2 in cadena1  # Comprova si cadena2 està dins de cadena1
print(es_subcadena('subcadena', 'cadena'))
print(es_subcadena('subcadena', 'text'))

#b) Retorne la que sigue anterior en ordre alfabètic. Per exemple, si rep 'kde' i 'gnome' ha de tornar 'gnome'.
def anterior_alfabetic(cadena1, cadena2):
    print("Cadenes:",cadena1,cadena2)
    return min(cadena1, cadena2)  # Utilitza min() per retornar la cadena alfabèticament anterior
print(anterior_alfabetic('kde', 'gnome'))

