#6 Pren el codi en Python següent, que emmagatzema una cadena: '
# cad = 'X-DSPAM-Confidence: 0.8475 Km'
# Utilitza find i llescat de cadenes (slicing) per extreure la porció de la
# cadena corresponent al número, i després fes servir la funció float per convertir la cadena
# extreta en un nombre en punt flotant.

cad = 'X-DSPAM-Confidence: 0.8475 Km' #cadena
principi = cad.find(":") +2 # find (:) +2 per a quedar-me amb el primer número
final = cad.find("Km") #find del Km
cad = cad[principi:final].strip() #Unico el principi amb el final de la cadena
final = float(cad) #Converteixo en float
print(final,type(final)) #Print del valor i del tipus

