import time

def main():
    hora = time.strftime("%H")
    minutos = time.strftime("%M")
    faltaHoras = 22 - (int(hora)+1)
    faltaMinutos = 59 - int(minutos)

    if int(hora) <= 19 :
        print("Son mas de las 7, puede ir a descansar")
    else:
        print(f"esta en su jornada laboral, {faltaHoras} horas y {faltaMinutos} minutos para salir")



if __name__ == "__main__":
    main()
