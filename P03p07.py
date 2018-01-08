print("CASILLAS BLANCAS O NEGRAS")

print("El programa nos va a indicar si 2 casillas del tablero son del mismo color.")

print("¿Cual es la primera casilla?")

numero_1=int(input("Dime un número, que representará la fila."))

if(numero_1 < 1) or (numero_1 > 8):

 print("Numero invalido")

 exit()
numero_2=int(input("Dime otro número, que representará la columna."))

if(numero_2 < 1) or (numero_2 > 8):

 print("Numero invalido")

 exit()
print("La primera casilla  es "+ str(numero_1)+ "," + str(numero_2))

if(numero_1%2!=0) and (numero_2%2!=0):

  print("La casilla es de color blanco")

  casilla1="blanca"

elif(numero_1%2==0) and (numero_2%2==0):

  print("La casilla es de color blanco")

  casilla1="blanca"

else:
  
 print("La casilla es de color negro")

  casilla1="negra"
print("¿Cúal es la segunda casilla ?")

numero_3=int(input("Dime un número, que representará la fila."))

if(numero_3 < 1) or (numero_3 > 8):

 print("Numero invalido")

 exit()

numero_4=int(input("Dime otro número, que representará la columna."))

if(numero_4 < 1) or (numero_4 > 8):

 print("Numero invalido")

 exit()
print("La segunda casilla  es "+ str(numero_3)+ "," + str(numero_4))

if(numero_3%2!=0) and (numero_4%2!=0):

  print("La casilla es de color blanco")

  casilla2="blanca"

elif(numero_3%2==0) and (numero_4%2==0):

  print("La casilla es de color blanco")

  casilla2="blanca"

else:
  
 print("La casilla es de color negro")

  casilla2="negra"

if(casilla1 == casilla2):

 print("Las casillas son del mismo color")

else:
  
 print("Las casillas son de distinto color")

 
