import clasica as cla
import fracciones as fra
import conversiones as conv
def la_calculadoreishon():
    inter = 0
    while inter != 1:
        try:
            menu = int(input("Ingrese 1 para entrar en la calculadora clasica \n2 para la calcuradora de fracciones\n3 para la calculadora de conversiones\no 4 para apagar: \n"))
            inter = 1
        except ValueError:
            print("El valor ingresado no es valido")
    inter = 0
    while menu != 4:
        if menu == 1:
            cla.cal_clasica()
        elif menu == 2:
            fra.cal_fracciones()
        elif menu == 3:
            conv.cal_conversiones()
        while inter != 1:
            try:
                menu = int(input("Ingrese 1 para entrar en la calculadora clasica \n2 para la calcuradora de fracciones\n3 para la calculadora de conversiones\no 4 para apagar: \n"))
                inter = 1
            except ValueError:
                print("El valor ingresado no es valido")
        inter = 0    
    print("apagado")

la_calculadoreishon()