import operaciones
def main():
    suma = operaciones.suma(2,2)
    resta =operaciones.resta(2,2)
    multiplicacion = operaciones.multiplicacion(2,2)
    division = int(operaciones.division(2,2))
    print(suma, resta, multiplicacion, division)

if __name__== "__main__":
    main()
