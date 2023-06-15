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