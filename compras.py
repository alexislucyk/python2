from mi_paquete.tienda import productos
from mi_paquete.cliente import clientes

menu=0
while menu==0:
    print(" -- Compras de Productos Informáticos -- ")
    print(" 1 - Registro de usuarios ")
    print(" 2 - Compra de productos ")
    print(" 9 - Salir ")
    seleccion=int(input("Seleccione una opcion: "))
    if seleccion==1: 
        print(" 1 - Registro ")
        while True:
            print('Para volver precione 9')
            clie_name=input("Ingresa tu nombre: ")
            if clie_name==9:
                break
            clie_apellido=input("Ingresa tu apellido : ")
            clie_dni=input("Ingresa tu dni : ")
            break

    elif seleccion==2:
        print(" 2 - Compra de productos ")
        while True:

            print(f'Item 1: {productos.prod1}')
            print(f'Item 2: {productos.prod2}')
            print(f'Item 3: {productos.prod3}')
            sel_opcion=int(input('Selecciona un producto: '))
            if sel_opcion==1:
                compra=productos.prod1
                print(f'El cliente: {clie_apellido}, {clie_name}, DNI: {clie_dni}')
                print(f'Compro {compra}')
                break
            elif sel_opcion==2:
                compra=productos.prod2
                print(f'compraste {compra}')
                break
            elif sel_opcion==3:
                compra=productos.prod3
                print(f'compraste {compra}')
                break

    elif seleccion==9:
        exit()
    else:
        print(" ## Opcion Invalida ##") 