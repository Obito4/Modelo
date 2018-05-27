def fibonaci(i):
    if i == 0:
        return 0
    if i == 1:
        return 1
    return fibonaci(i-1) + fibonaci(i-2)
n=int(input("Dime un número y te diré a que número de la sucesión de fibonacci corresponde"))
print(fibonaci(i))