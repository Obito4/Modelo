primero=int(input("¿Cual es el primero?"))

segundo=int(input("¿Cual es el segundo?"))
 
tercero=int(input("¿Cual es el tercero?"))

if (primero<segundo)and (primero<tercero):

 print(primero)

else:

  if segundo>tercero:
 
    print(tercero)

  if tercero>segundo:
 
   print(segundo)