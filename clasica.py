def cal_clasica():
    menu = 1
    inter = 0
    if menu == 1:
        while inter != 1:
            try:
                valor_1 = float(input("ingrese el primer valor: "))
                inter = 1
            except ValueError:
                print("El valor ingresado no es valido")
        inter = 0
        signo = input("ingrese la cuenta que quiere hacer (+, -, *, /): ")
        while signo != "=":
            if signo == "+":
                while inter != 1:
                    try:
                        valor_2 = float(input("ingrese el otro valor: "))
                        valor_1 += valor_2
                        inter = 1
                    except ValueError:
                        print("El valor ingresado no es valido")
                inter = 0
            elif signo == "-":
                while inter != 1:
                    try:
                        valor_2 = float(input("ingrese el otro valor: "))
                        valor_1 = valor_1 - valor_2
                        inter = 1
                    except ValueError:
                        print("El valor ingresado no es valido")
                inter = 0
            elif signo == "/":
                while inter != 1:
                    try:
                        valor_2 = float(input("ingrese el otro valor: "))
                        valor_1 = valor_1 / valor_2
                        inter = 1
                    except ValueError:
                        print("El valor ingresado no es valido")
                    except ZeroDivisionError:
                        print("Se ha intentado dividir por cero (0) vuelve a intentarlo")
                inter = 0
            elif signo == "*":
                while inter != 1:
                    try:
                        valor_2 = float(input("ingrese el otro valor: "))
                        valor_1 = valor_1 * valor_2
                        inter = 1
                    except ValueError:
                        print("El valor ingresado no es valido")
                inter = 0
            else:
                print("Eso no corresponde a ninguno de los simbolos permitidos")
            signo = input("si quiere seguir operando ingrese otro simbolo, diferente de =: ")
        print(f"{valor_1}")
