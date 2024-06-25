GENEROS = ["Ficción", "No Ficción", "Ciencia"]


def registrarLibro(Libros):
    titulo = input("Ingrese el titulo del libro : ")
    generoLibro  = input("Ingrese el genero de libro: (Ficcion / No ficción / Ciencia)").lower()
    while generoLibro   not in GENEROS:
        print("Opcion no valida .Ingrese una de los generos de libro (Ficcion / No ficción / Ciencia)")
    precio = int(input("Ingrese el valor del libro : "))

  


 
    







def listarLibros(Libros):
    for Libro in listarLibros:
        print("Los libros son : " [Libros])

    
  

def registrarVentas(Libros):
    print()


def imprimirReporteVentas(Libros):
    print()
    