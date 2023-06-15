def resto_hex(resto):
    if resto == 10:
        ret_val = "A"
    elif resto == 11:
        ret_val = "B"
    elif resto == 12:
        ret_val = "C"
    elif resto == 13:
        ret_val = "D"
    elif resto == 14:
        ret_val = "E"
    elif resto == 15:
        ret_val = "F"
    return ret_val
    
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
        signo = input("ingrese la cuenta que quiere hacer (+, -, x, /): ")
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
                inter = 0
            elif signo == "x" or "X":
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

def cal_fracciones():
    menu = 3
    if menu == 3:
        flag = True
        while flag == True:
            try:
                num_1 = float(input("Ingrese el numerador: "))
                den_1 = float(input("Ingrese el denominador: "))
                signo = input("Ingrese el signo + - * / para operar seguir operando o '=' para terminar la operacion: ")
                while signo != "=":
                    if signo == "+":
                        try:
                            num_2 = float(input("Ingrese otro numerador: "))
                            den_2 = float(input("Ingrese otro denominador: "))
                            num_1 = (num_1*den_2) + (num_2*den_1)
                            den_1 = den_1 * den_2
                            signo = input("Ingrese el signo + - * / para operar seguir operando o '=' para terminar la operacion: ")
                        except ValueError:
                            print("El valor ingresado no corresponde a un numero")
                    elif signo == "-":
                        try:
                            num_2 = float(input("Ingrese otro numerador: "))
                            den_2 = float(input("Ingrese otro denominador: "))
                            num_1 = (num_1*den_2) - (num_2*den_1)
                            den_1 = den_1 * den_2
                            signo = input("Ingrese el signo + - * / para operar seguir operando o '=' para terminar la operacion: ")
                        except ValueError:
                            print("El valor ingresado no corresponde a un numero")
                    elif signo == "*":
                        try:
                            num_2 = float(input("Ingrese otro numerador: "))
                            den_2 = float(input("Ingrese otro denominador: "))
                            num_1 = num_1 * num_2
                            den_1 = den_1 * den_2
                            signo = input("Ingrese el signo + - * / para operar seguir operando o '=' para terminar la operacion: ")
                        except ValueError:
                            print("El valor ingresado no corresponde a un numero")
                    elif signo == "/":
                        try:
                            num_2 = float(input("Ingrese otro numerador: "))
                            den_2 = float(input("Ingrese otro denominador: "))
                            num_1 = num_1 * den_2
                            den_1 = den_1 * num_2
                            signo = input("Ingrese el signo + - * / para operar seguir operando o '=' para terminar la operacion: ")
                        except ValueError:
                            print("El valor ingresado no corresponde a un numero")
                    else:
                        print ("El simbolo ingresado no corresponde a uno solicitado")
                contador = 2
                while contador <= 10:
                    if num_1 % contador == 0 and den_1 % contador == 0:
                        num_1 = num_1 / contador
                        den_1 = den_1 / contador
                    else:
                        contador += 1
                if den_1 == 0:
                    print (f"Tu cuenta total es {num_1}/{den_1} lo cual es raro ya que es dividirlo por la nada misma")
                else:
                    print (f"Tu cuenta total es {num_1}/{den_1}")
                flag = False
            except ValueError:
                print("El valor ingresado no corresponde a un numero")
            
            
def cal_conversiones():
    menu = 3
    inter = 0
    if menu == 3:
        while inter != 1:
            try:
                valor_1 = int(input("Ingrese el valor en sistema decimal que quiere convertir: "))
                inter = 1
            except ValueError:
                print("El valor ingresado no es valido")
        inter = 0
        while inter != 1:
            try:
                sist_num = int(input("Ingrese un numero dependiendo a que sistema numerico quiere convertir el numero\n 1 Binario \n 2 Octal \n 3 Hexadecimal\n"))
                inter = 1
            except ValueError:
                print("El valor ingresado no es valido")
        if sist_num == 1:
            res_conv = ""
            while valor_1 >= 2:
                resto = valor_1 % 2
                res_conv = str(f"{resto}"+res_conv)
                valor_1 = (valor_1 // 2)   
            res_conv = str(f"{valor_1}"+res_conv)
            print(f"{res_conv}")
        if sist_num == 2:
            res_conv = ""
            while valor_1 >= 8:
                resto = valor_1 % 8
                res_conv = str(f"{resto}"+res_conv)
                valor_1 = (valor_1 // 8)    
            res_conv = str(f"{valor_1}"+res_conv)
            print(f"{res_conv}")
        if sist_num == 3:
            res_conv = ""
            while valor_1 >= 16:
                resto = valor_1 % 16
                if resto >= 10:
                    res_conv = str(resto_hex(resto)+res_conv)
                    valor_1 = (valor_1 // 16)
                else:
                    res_conv = str(f"{resto}"+res_conv)
                    valor_1 = (valor_1 // 16)
            if valor_1 >= 10:
                resto = valor_1
                res_conv = str(resto_hex(resto)+res_conv)
            else:
                res_conv = str(f"{valor_1}"+res_conv)
            print(f"{res_conv}")

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
            cal_clasica()
        elif menu == 2:
            cal_fracciones()
        elif menu == 3:
            cal_conversiones()
        while inter != 1:
            try:
                menu = int(input("Ingrese 1 para entrar en la calculadora clasica \n2 para la calcuradora de fracciones\n3 para la calculadora de conversiones\no 4 para apagar: \n"))
                inter = 1
            except ValueError:
                print("El valor ingresado no es valido")
        inter = 0    
    print("apagado")
    
la_calculadoreishon()