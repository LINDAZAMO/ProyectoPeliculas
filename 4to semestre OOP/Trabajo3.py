class Cantante:
    def __init__(self):
        self.nombre = input("Favor de ingresar el nombre del cantante: ")
        self.__mejorcancion = ""

    def setcantante(self):
        self.nuevacancion = input("Favor de ingresar su mejor cancion: ")
        self.__mejorcancion = self.nuevacancion

    def getcantante(self):
        return self.__mejorcancion


class Cuenta:
    def __init__(self):
        self.__titular = input("¿Quién es el titular? ")
        self.__cantidad = int(input("La cantidad a ingresar es: "))

    def set_ingresar(self):
        self.nuevacantidad = int(input("Cuanta cantidad desea ingresar: "))
        if self.nuevacantidad <= 0:
            print("Error, NO se pueden ingresar esa cantidad porque es negativa")
        else:
            self.__cantidad = self.__cantidad + self.nuevacantidad

    def set_retirar(self):
        self.retiro = int(input("Cuánto desea retirar: "))
        self.__cantidad = self.__cantidad - self.retiro

    def get_mostrarinfo(self):
        print("La cuenta de:", self.__titular)
        print("Tiene la cantidad de:", self.__cantidad)


class Trabajador:
    def __init__(self):
        self.__num = 0
        self.__nombre = ""
        self.__apellidos = ""
        self.__SueldoMensual = 0
        self.__Cargo = ""
        self.bandera = 0

    def set_Informacion(self):
        self.numero = int(input("Ingrese el número de empleado: "))
        self.nomb = input("Ingrese el nombre del empleado: ")
        self.ape = input("Ingrese los apellidos del empleado: ")
        self.sueldomes = float(input("Ingresar el sueldo mensual del empleado: "))
        self.puesto = input("Ingresar el cargo (puesto) del empleado: ")
        self.__num = self.numero
        self.__nombre = self.nomb
        self.__apellidos = self.ape
        self.__SueldoMensual = self.sueldomes
        self.__Cargo = self.puesto
        self.bandera = 1

    def get_info(self):
        return self.__num, self.__nombre, self.__apellidos, self.__SueldoMensual, self.__Cargo

    def desplegarTodo(self):
        if self.bandera == 1:
            print("Número de empleado:", self.__num,
                  "\nNombre Completo:", self.__nombre, self.__apellidos,
                  "\nSueldo mensual:", self.__SueldoMensual,
                  "\nCargo:", self.__Cargo)
        else:
            print("Error, NO se ha introducido información del empleado")


# Ejercicio 1: Clase de Cantante
print("Ejercicio 1: Clase de Cantante")
Artista = Cantante()
Artista.setcantante()
print("La mejor canción de:", Artista.nombre, "es", Artista.getcantante())
print()

# Ejercicio 2: Clase de cuenta
print("Ejercicio 2: Clase de Cuenta")
contador = 0
Biron = Cuenta()
while contador < 2:  # Utilizar cada método dos veces
    Biron.get_mostrarinfo()
    Biron.set_ingresar()
    Biron.set_retirar()
    contador = contador + 1
Biron.get_mostrarinfo()  # Ver la información después de utilizar dos veces cada método
print()

# Ejercicio 3: Clase de Trabajador
print("Ejercicio 3: Clase de Trabajador")
biron = Trabajador()
biron.set_Informacion()
biron.desplegarTodo()
