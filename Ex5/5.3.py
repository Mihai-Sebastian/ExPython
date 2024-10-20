#3. Reescriu el programa que demana a l'usuari una llista de números i imprimeix en pantalla el màxim i mínim dels nombres introduïts,
# quan l'usuari introdueix "fi". Escriu ara el programa de manera que emmagatzeme els números que l'usuari introdueixi en una llista i
# usa les funcions max() i min() per calcular els nombres màxim i mínim després que el bucle acabe.

def maxmin():
   numeros = []  # Llista per guardar els números

   while True: #While True per entrar al bucle
       entrada = input("Introdueix un número: ") #Input del usuari
       if entrada.lower() == "fi":  # Acaba el bucle si l'usuari escriu "fi"
           break #Surt del bucle
       try:
           numero = float(entrada)  # Converteix l'entrada a número (float)
           numeros.append(numero)  # Afegeix el número a la llista
       except:
           print("Entrada no vàlida. Introdueix un número o 'fi' per acabar.")
   if numeros:  # Comprova si la llista té números
       print("Màxim:", max(numeros)) #Print del maxim
       print("Mínim:", min(numeros)) #Print del mínim
   else:
       print("No has introduït cap número.")
maxmin() #Crida de la funció
