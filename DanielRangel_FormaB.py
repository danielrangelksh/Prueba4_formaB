datos={
    "comprador": [
        {
            "nombre": "daniel rangel",
            "tipo_de_entrada": "G",
            "codigo": "ADc123",
        }
    ]
}

def comprar_entrada():
    "Esta función permite acceder al comprador."
    while True:
        try:
            nombre=input("Ingrese su nombre completo: ")
            for i in datos["comprador"]:
                if nombre==i["nombre"]:
                    print("El nombre ya se encuentra ingresado! ")
                    return
                else:
                    print("Nombre ingresado correctamente.")
        except ValueError:
            print("Ingrese un numbre con carácteres.")
            return

        try:
            tipo_entrada=input("¿Desea entrada general o VIP? (G/V): ")
            if tipo_entrada == "V" or tipo_entrada == "v":
                print("La entrada es VIP")
            elif tipo_entrada == "G" or tipo_entrada=="g":
                print("La entrada es General")
            else:
                print("Ingrese opción correcta.")
        except ValueError:
            print("Debe ingresar carácteres no númericos.")
            return

        try: 
            codigo=input("Ingrese su código de compra: ")
            if len(codigo)<6:
                print("El código debe contener más de seis carácteres.")
                return
            elif codigo is not codigo.isalpha and codigo is not codigo.isdigit:
                print("El codigo debe llevar carácteres alfanumericos")
            else:
                print("Código ingresado correctamente. ")
        except ValueError:
            print("El código debe llevar carácteres alfanumericos. ")
            return
        
        compra_agregar= {
            nombre == "nombre", 
            tipo_entrada == "tipo_de_entrada", 
            codigo == "codigo"
            }
        
        datos["comprador"].append(compra_agregar)
        print("Comprador ingresado correctamente!")
        break

def consulta_comprador():
    "Función que entrega los datos del comprador buscandolo por su nombre."
    try:    
        nombre=input("Ingrese el nombre del comprador: ")
        for i in datos["comprador"]:
            if nombre == i["nombre"]:
                print("Aquí tiene los datos!")
                print(f"Tipo de entrada {i['tipo_de_entrada']}, código de confirmación: {i['codigo']}.")
            else:
                print("El comprador no se encuentra")
                return
    except ValueError:
        print("El nombre debe contener carácteres. ")
        return

def cancelar_compra():
    "Función que cancela la compra borrando los datos del comprador ingresando su nombre."
    try:
        nombre=input("Ingrese el nombre del comprador: ")
        for i in datos["comprador"]:
            if nombre==i['nombre']:
                datos["comprador"].remove
                print("¡Compra cancelada!")
            else:
                print("No se encuentra el nombre, no se pudo cancelar la compra.")
                return
    except ValueError:
        print("ingrese carácteres.")
        return

def menu():
    while True:
        print("Bienvenido al menú de compra para el concierto del Conejo Simpático!")
        print("[1] Comprar entrada")
        print("[2] Consultar comprador")
        print("[3] Cancelar compra")
        print("[4] Salir")
        try:
            opcion=int(input("Ingrese una opción: "))
        except ValueError:
            print("Ingrese un número entero.")
            continue
        
        if opcion == 1:
            comprar_entrada()
        elif opcion == 2:
            consulta_comprador()
        elif opcion == 3:
            cancelar_compra()
        elif opcion == 4:
            print("Saliendo del programa...")
            break
        else:
            print("Ingrese una opción correcta.")
            continue

menu()