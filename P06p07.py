numero = 0

maximo = 0

while True:

  numero += 1

  i = int(input("Dime un n�mero"))

  if i < maximo:
 
   maximo = maximo
 
 else:
    
   maximo = i

 if i == 0:
    
   break

print("El n�mero de n�meros recibidos es" +" "+ str(numero-1))

print("El n�mero maximo de la cadena es" +" "+ str(maximo))