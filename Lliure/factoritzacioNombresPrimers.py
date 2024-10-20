#Factorització en nombres primers
def multiplicarLlista(llista):
   resultat=1
   for i in llista:
       resultat*=i
   return resultat

n=int(input())
n2=n
pivot=2
llista=[]
while True:
   if multiplicarLlista(llista)==n:
       break
   if n2 % pivot ==0 and multiplicarLlista(llista) !=n:
       llista.append(pivot)
       n2/=pivot
   else:
       pivot+=1
print(llista)

