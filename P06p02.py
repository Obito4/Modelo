N=int(input("Dime un n�mero mayor que 2"))

Divisor=2
while True:

  if N/Divisor==N//Divisor:

    print(str(Divisor) +" "+ "es el menor divisor")

    break

  Divisor+=1