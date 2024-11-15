class Perro:
    def __init__(self, raza):
        self.raza = raza
        print("Raza del perro:", self.raza)
class Estudiante:
    def __init__(self, nombre, calificacion):
        self.nombre = nombre
        self.calificacion = calificacion
    def AproboMateria(self):
        print("Nombre del estudiante:", self.nombre)
        if self.calificacion >= 60:
            print("Calificacion:", self.calificacion,"APROBO")
        else:
            print("Calificacion:", self.calificacion,"REPROBO")

class Pelicula:
    def __init__(self, titulo, sinopsis):
        self.titulo = titulo
        self.sinopsis = sinopsis
    def MostrarInformacion(self):
        print("Título:", self.titulo)
        print("Sinopsis:", self.sinopsis)
        perro = Perro("Bulldog")


estudiante = Estudiante("Juan", 60)
estudiante.AproboMateria()
titulo = input("Ingrese el título de la película:")
sinopsis = input("Ingrese la sinopsis de la película:")
pelicula = Pelicula(titulo, sinopsis)
pelicula.MostrarInformacion()