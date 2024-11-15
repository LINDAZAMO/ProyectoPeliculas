class Trabajador:
    def __init__(self):
        self.nombre = input("Ingrese su nombre: ")
        self.edad = int(input("Ingrese su edad: "))

    def info(self):
        print("Nombre:", self.nombre)
        print("Edad:", str(self.edad))


class Contador(Trabajador):
    descripcion = "Soy contador y me gusta ver los estados financieros"

    def informacion(self):
        super().info()
        print("Me llamo " + self.nombre, "tengo " + str(self.edad), "y " + self.descripcion)


class Ingeniero(Trabajador):
    descripcion = "Soy ingeniero y me gusta automatizar procesos"

    def informacion(self):
        super().info()
        print("Me llamo " + self.nombre, "tengo " + str(self.edad), "y " + self.descripcion)


class Aviador(Trabajador):
    descripcion = "Soy piloto aviador y trabajo en Volaris"

    def informacion(self):
        super().info()
        print("Me llamo " + self.nombre, "tengo " + str(self.edad), "y " + self.descripcion)


class Barrendero(Trabajador):
    descripcion = "Soy barrendero pero de mi propia casa"

    def informacion(self):
        super().info()
        print("Me llamo " + self.nombre, "tengo " + str(self.edad) + " y " + self.descripcion)


print("Ejercicio 1: Herencia con clase Trabajador")
Hijo1 = Contador()
Hijo2 = Ingeniero()
Hijo3 = Aviador()
Hijo4 = Barrendero()

print()
Hijo1.informacion()
Hijo2.informacion()
Hijo3.informacion()
Hijo4.informacion()


# %%

class Figura:
    def NombreFigura(self):
        self.nombre = input("Nombre de la figura: ")


class Circulo(Figura):
    def __init__(self):
        self.NombreFigura()
        self.pi = 3.1416

    def CalcularArea(self):
        print("La figura es:", self.nombre)
        self.radio = int(input("Ingresa tu radio: "))
        self.area = self.pi * (self.radio ** 2)
        print("El área es:", self.area)
        print("")


class Cuadrado(Figura):
    def __init__(self):
        self.NombreFigura()

    def CalcularArea(self):
        print("La figura es:", self.nombre)
        self.lado = int(input("Ingresa el lado del cuadrado: "))
        self.area = self.lado * self.lado
        print("El área es:", self.area)
        print("")


class Rectangulo(Figura):
    def __init__(self):
        self.NombreFigura()

    def CalcularArea(self):
        print("La figura es:", self.nombre)
        self.base = int(input("Ingresa la base del rectángulo: "))
        self.altura = int(input("Ingresa la altura del rectángulo: "))
        self.area = self.base * self.altura
        print("El área es:", self.area)
        print("")


class Triangulo(Figura):
    def __init__(self):
        self.NombreFigura()

    def CalcularArea(self):
        print("La figura es:", self.nombre)
        self.base = int(input("Ingresa la base del triángulo: "))
        self.altura = int(input("Ingresa la altura del triángulo: "))
        self.area = (self.base * self.altura) / 2
        print("El área es:", self.area)


print("Ejercicio 2: Herencia con la clase Figura")
circulo = Circulo()
circulo.CalcularArea()

cuadrado = Cuadrado()
cuadrado.CalcularArea()

rectangulo = Rectangulo()
rectangulo.CalcularArea()

triangulo = Triangulo()
triangulo.CalcularArea()

# %%

print("Ejercicio 3: Polimorfismo con la clase Trabajador")


def mostrar_informacion_completa(objeto):
    objeto.informacion()


# Crear nuevas variables
persona1 = Contador()
mostrar_informacion_completa(persona1)

print()
persona2 = Ingeniero()
mostrar_informacion_completa(persona2)

print()
persona3 = Aviador()
mostrar_informacion_completa(persona3)

print()
persona4 = Barrendero()
mostrar_informacion_completa(persona4)

# %%

print("Ejercicio 4: Polimorfismo con la clase Figura")


def ObtenerArea(figura):
    figura.CalcularArea()


figura1 = Circulo()
ObtenerArea(figura1)

figura2 = Cuadrado()
ObtenerArea(figura2)

figura3 = Rectangulo()
ObtenerArea(figura3)

figura4 = Triangulo()
ObtenerArea(figura4)
