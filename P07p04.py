def fibonaci(i):
    if i == 0:
        return 0
    if i == 1:
        return 1
    return fibonaci(i-1) + fibonaci(i-2)
n=int(input("Dime un n�mero y te dir� a que n�mero de la sucesi�n de fibonacci corresponde"))
print(fibonaci(i))