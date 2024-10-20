# 7. Escriu 2 funcions per, donada una cadena de caràcters:
# a) Retornar la cadena extreent cada dos caràcters del paràmetre. Ex .: 'recta' hauria de retornar 'rca'

def extreure_cada_dos(caracters):
    return caracters[::2]  # Retorna la cadena saltant cada 2 caràcters
print(extreure_cada_dos('recta'))

# b) Retornar la cadena concatenant el paràmetre en un sentit i en sentit invers. Ex: 'reflex' torna 'reflexxelfer'.
def concatenar_sentits(caracters):
    return caracters + caracters[::-1]  # Concatena la cadena amb la seva inversa
print(concatenar_sentits('reflex'))
