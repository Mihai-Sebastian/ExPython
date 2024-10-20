#1.2. Escriu un programa per demanar-li a l'usuari el nombre d'hores i la tarifa per hora per calcular el salari brut.
hores=int(input("Introdueix el nombre d'hores treballades: "))
tarifa=float(input("Introdueix la tarifa: "))
print("Salari:", round(hores*tarifa,2)) #multiplica les hores per la tarifa i fa un round per mostrar sols 2 decimals.