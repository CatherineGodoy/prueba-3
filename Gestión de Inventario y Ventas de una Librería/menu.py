import funciones as fn 

Libros = []
GENEROS = ["Ficción", "No Ficción", "Ciencia"]

while True:
    print("Bienvenido a su Rincón del libro")
    print("(1) Registrar Libro")
    print("(2)Listar todos los libros")
    print("(3)Registrar venta")
    print("(4)Imprimir reporte de ventas")
    print("(5)Salir")

    opcion = int(input("Ingrese una opción : "))

    if opcion == 1:
        titulo = input("iNGRESE EL TITULO DEL LIBRO : ")
        genero = input("INGRESE EL GENERO DEL LIBRO : ")
        while genero  not in GENEROS:
            print("Opcion no valida . Ingrese uno de los generos de libro (Ficción / No ficción / Ciencia)")
            break
        precio = int(input("INGRESE EL VALOR DEL LIBRO : "))
        fn.registrarLibro(Libros)

    elif opcion == 2:
        fn.listarLibros
        
    elif opcion == 3:
        fn.registrarVentas
        print()
    elif opcion == 4:
        fn.imprimirReporteVentas
        print()
    elif opcion == 5:
        print("Gracias por su preferencia , Hasta Luego")
        break
    else:
        print("Por Favor ingrese una opción valida")
    
