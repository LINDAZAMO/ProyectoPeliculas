#Ejemplo con ciclo for

numeros = [1, 2, 3, 4, 5]

for numero in numeros:
    cuadrado = numero ** 2
    print(f"El cuadrado de {numero} es {cuadrado}")

# Usamos un ciclo for para recorrer la lista de números
# Numero es la variable que ira tomando el valor de cada elemento de la lista numeros uno por uno.
# El ciclo repertira el bloque de codigo denntro de el por cada elemento de la lista
# Calculamos el cuadrado de numero usando ** 2, que es el operador de potencia en python
# La f al inicio del print permite formatear la cadena, de modo que podemos incluir el valor de las variables numero y cuadrado dentro del texto.



#Ejemplo de While

contador = 1

# Mientras el valor de contador sea menor o igual a 5, el ciclo se repite
while contador <= 5:
    print(f"Este es el intento número {contador}")
    contador += 1  # Incrementa el valor de contador en 1 en cada iteración

#Iniciamos una variable llamada contador con el valor 1. Esta variable será usada para controlar cuántas veces se repite el ciclo.
#El ciclo while se repite mientras contador sea menor o igual a 5. Si contador llega a ser mayor que 5, el ciclo se detiene.
#Esta línea incrementa el valor de contador en 1 en cada repetición del ciclo. Es lo mismo que escribir contador = contador + 1.
# Esto es importante para que eventualmente la condición contador <= 5 sea falsa y el ciclo se detenga, evitando un ciclo infinito.



#HERENCIAA
# Clase padre
class Animal:
    def comer(self):
        print("El animal está comiendo")

# Clase hija
class Perro(Animal):
    def ladrar(self):
        print("El perro está ladrando")

# Creamos un objeto de la clase Perro
mi_perro = Perro()

# El perro puede usar métodos de la clase Animal (porque hereda de Animal)
mi_perro.comer()  # Esto viene de la clase Animal

# El perro también tiene su propio método
mi_perro.ladrar()  # Esto es específico de la clase Perro





#POLIMORFISMOOOO

# Clase padre
class Animal:
    def hacer_sonido(self):
        pass  # Esto se llenará en las clases hijas

# Clase hija 1
class Perro(Animal):
    def hacer_sonido(self):
        print("El perro ladra: ¡Guau!")

# Clase hija 2
class Gato(Animal):
    def hacer_sonido(self):
        print("El gato maúlla: ¡Miau!")

# Clase hija 3
class Pajaro(Animal):
    def hacer_sonido(self):
        print("El pájaro canta: ¡Pío pío!")

# Creamos una lista de diferentes animales
animales = [Perro(), Gato(), Pajaro()]

# Usamos polimorfismo: todos usan el mismo método, pero el resultado es diferente
for animal in animales:
    animal.hacer_sonido()




#Encapsulamiento
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo público
        self.__edad = edad    # Atributo privado (oculto)

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.__edad}")  # Aquí podemos acceder al atributo privado

    def cambiar_edad(self, nueva_edad):
        if nueva_edad > 0:
            self.__edad = nueva_edad   # Cambiamos la edad a través de este método
        else:
            print("La edad no puede ser negativa")

# Crear un objeto de la clase Persona
persona1 = Persona("Ana", 30)

# Acceder a los datos a través de un método público
persona1.mostrar_info()

# Intentar cambiar la edad usando el método
persona1.cambiar_edad(35)
persona1.mostrar_info()

# Intentar acceder al atributo privado directamente (esto fallará)
print(persona1.__edad)  # Esto dará error




#ABSTRACCION

from abc import ABC, abstractmethod


# Clase abstracta
class Animal(ABC):  # Hereda de ABC (Abstract Base Class)

    @abstractmethod
    def hacer_sonido(self):
        pass  # Este método es abstracto, las clases hijas deben implementarlo


# Clase hija 1
class Perro(Animal):
    def hacer_sonido(self):
        print("El perro hace: ¡Guau!")


# Clase hija 2
class Gato(Animal):
    def hacer_sonido(self):
        print("El gato hace: ¡Miau!")


# Clase hija 3
class Vaca(Animal):
    def hacer_sonido(self):
        print("La vaca hace: ¡Muuu!")


# Ahora usamos abstracción: trabajamos solo con lo esencial
def hacer_sonido_animal(animal):
    animal.hacer_sonido()


# Creamos objetos de las clases hijas
perro = Perro()
gato = Gato()
vaca = Vaca()

# Llamamos a la función que usa abstracción
hacer_sonido_animal(perro)  # Guau
hacer_sonido_animal(gato)  # Miau
hacer_sonido_animal(vaca)  # Muuu