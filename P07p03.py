import math
def potencia(x,n):
  if n == 0:
      return 1
  return x * potencia(x,(n-1))
def d(x1,x2,y1,y2):
  solucion=math.sqrt(potencia((x2-x1),2) + potencia((y2-y1),2))
  return solucion
x1=int(input("Dime la posicion de x en el punto 1"))
y1=int(input("Dime la poscion de y en el punto 1"))
x2=int(input("Dime la posicion de x en dl punto 2"))
y2=int(input("Dime la posicion de y en el punto 2"))
print(d(x1,x2,y1,y2))