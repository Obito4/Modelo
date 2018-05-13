numero = 0

suma = 0

media = 1

while True:

  numero += 1

  i = int(input("Dime un número"))

  suma = suma + i

  if i == 0:
 
   break

print("El número de números introducidos es" +" "+ str(numero-1))

print("La suma de todos los números introducidos son" +" " +str(suma))

media = suma/(numero-1)

print("La media de la secuencia es" +" "+ str(media))