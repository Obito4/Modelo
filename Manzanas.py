estudiantes=int(input("N�mero de alumnos"))
manzanas=int(input("Manzanas compradas"))
sobrantes=manzanas-estudiantes
estudiantemanzana=manzanas//estudiantes
cestamanzana=manzanas%estudiantes
print("Las manzanas por estudainte son " +str(estudiantemanzana))
print("las manzanas que quedan en la cesta " +str(cestamanzana))
