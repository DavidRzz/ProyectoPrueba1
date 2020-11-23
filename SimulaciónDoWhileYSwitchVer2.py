print ("Switch case en python")



while True:

    op=int(input("Seleccionar una opción:"))
    if op==1:
    
        while True:
            print ("Conversion de grados centigrados a Kelvin")
            grados=float(input("Grados centigrados"))
            Kelvin=grados+273.15
            print ("Grados Kelvin: ", format(Kelvin, ".2f"))
            salir=int(input("Realizar otra consulta Si=1, No=2: "))
            if salir!=1:
                break
    
    
    elif op==2:
        
        while True:
            print ("Conversion de metros cubicos a litros")
            metroscubicos=float(input("Metros cúbicos "))
            litros=metroscubicos+1000
            print ("litros", format(litros, ".2f"))
            salir=int(input("Realizar otra consulta Si=1, No=2: "))
            if salir!=1:
                break
    
    
    elif op==3:
        
        while True:
            print ("Area de cuadrado")
            lado=float(input("lados: " ))
            area=lado*lado
            print ("Area:  ", format(area, ".2f"))
            salir=int(input("Realizar otra consulta Si=1, No=2: "))
            if salir!=1:
                break
    
    else:
        print ("No selecciono opciones")
    
    again=int(input("¿Deseas seleccionar otra opción? si=1 no=2 "))
    if again!=1:
        break
print ("Adios")