numero = 0

suma = 0

media = 1

while True:

  numero += 1

  i = int(input("Dime un n�mero"))

  suma = suma + i

  if i == 0:
 
   break

print("El n�mero de n�meros introducidos es" +" "+ str(numero-1))

print("La suma de todos los n�meros introducidos son" +" " +str(suma))

media = suma/(numero-1)

print("La media de la secuencia es" +" "+ str(media))