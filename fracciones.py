def cal_fracciones():
    menu = 3
    if menu == 3:
        flag = True
        while flag == True:
            try:
                num_1 = int(input("Ingrese el numerador: "))
                den_1 = int(input("Ingrese el denominador: "))
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
            