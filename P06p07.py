numero = 0

maximo = 0

while True:

  numero += 1

  i = int(input("Dime un número"))

  if i < maximo:
 
   maximo = maximo
 
 else:
    
   maximo = i

 if i == 0:
    
   break

print("El número de números recibidos es" +" "+ str(numero-1))

print("El número maximo de la cadena es" +" "+ str(maximo))