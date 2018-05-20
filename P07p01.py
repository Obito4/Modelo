import math
def d(x1,x2,y1,y2):
  solucion=math.sqrt((x2-x1)**2 + (y2-y1)**2)
  return solucion
x1=int(input("Dime la posiscion de x en el punto 1"))
y1=int(input("Dime la posiscion de y en el punto 1"))
x2=int(input("Dime la posiscion de x en el punto 2"))
y2=int(input("Dime la posiscion de y en el punto 2"))
print(d(x1,x2,y1,y2))