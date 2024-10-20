# 3.  Dissenyeu un algorisme que calcule una aproximació al número π mitjançant el producte de Wallis:
# L’entrada a l’algorisme serà el número de termes (fraccions) a calcular, i la sortida serà l’aproximació al número π
# segons el producte de Wallis en el número de termes especificat.

#Funció que agafa la variable termes que li passem.
def producteWalis(termes):
    #Declaració de les variables
    n=1
    f1=1
    f2=1
    #For del rang dels termes indicats.
    for i in range(termes):
        #f1 es el numerador i f2 el denominador
        f1*=termes*(n**2) # Aplico les formules
        f2*=termes*(n**2)-1
        n+=1 #Suma de +1 a n per cada iteració
    return round(f1/f2,4) #return de la divisió del numerador i el denominador utilitzant round per retornar sols 4 decimals

#Crida de la funció
print("Nombre pi aproximat:", producteWalis(termes=int(input("Indica els termes: "))))
