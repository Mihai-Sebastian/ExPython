
#Nombres amics
def Divisors(n):
   divisors=[]
   for i in range(1, n):
       if n % i == 0:
           divisors.append(i)
   return divisors
n1=int(input())
n2=int(input())

if sum(Divisors(n1)) == n2 and sum(Divisors(n2)) == n1:
   print("Números amics")
else:
   print("No son amics")

