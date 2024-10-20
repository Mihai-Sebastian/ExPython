#5 Donada una llista de números enters, escriu una funció que retorne una llista en tots els que siguen primers.

def nombres_primers(llista):
    print(llista)
    primers = [] #Creo una llista a on afegiré els números primers
    for n in llista:
        if n > 1:
            for i in range(2, n):
                if n % i == 0: #Divideix tots els números menys l'1 i el mateix número entre 2, si el resultat és 0 significa que no és un número primer i trenca el bucle
                    break
            else:  # Si no trenca el bucle és un número primer que s'afegeix a la llista
                primers.append(n)
    return primers #retorna la llista
print(nombres_primers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
