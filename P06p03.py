x = int(input("Dime los Km que quieres correr"))

y= int(input("Dime los Km que debes que correr"))

Dias = 0

while x < y:

  i = int(x) * 0.1

  x = x+i
  
  Dias += 1

print("El"+str (Dias) + " dia correre" +str(int(x+1)) + " "  +"km")