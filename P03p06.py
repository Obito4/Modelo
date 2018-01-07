print("MOVIMIENTO DE LA TORRE")
print("El programa nos va a indicar si la torre puede moverse a una determinada casilla o no dependiendo de donde se encuentre. El tablero tiene 8 filas y 8 columnas.")
print("¿Cúal es la casilla de origen?")
numero_1=int(input("Dime un número, que representará la fila."))

if(numero_1 < 1) or (numero_1 > 8):

 print("Numero invalido")

 exit()
numero_2=int(input("Dime otro número, que representará la columna."))

if(numero_2 < 1) or (numero_2 > 8):

 print("Numero invalido")

 exit()
print("La casilla de origen es "+ str(numero_1)+ "," + str(numero_2))

print("¿Cúal es la casilla de destino?")

numero_3=int(input("Dime un número, que representará la fila."))

if(numero_3 < 1) or (numero_3 > 8):

 print("Numero invalido")

 exit()
numero_4=int(input("Dime otro número, que representará la columna."))

if(numero_4 < 1) or (numero_4 > 8):

 print("Numero invalido")

 exit()
print("La casilla de destino es "+ str(numero_3)+ "," + str(numero_4))

print("-----------------")

print("Calculando si la torre se puede mover de la casilla "+ str(numero_1)+ "," + str(numero_2) +
 " a la casilla "+ str(numero_3)+ "," + str(numero_4))

print("-----------------")
if(numero_1==numero_3) or (numero_2==numero_4):

  print(" La torre se puede mover.")

else:

  print(" La torre no se puede mover.")
 
