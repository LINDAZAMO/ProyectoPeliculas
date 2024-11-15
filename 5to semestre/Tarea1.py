#Programación para la extracción de Datos
#Vazquez Zamora Linda Jaqueline
#Tarea 1

class Estadistica:
    def calcular_frecuencia(self, numeros):
        self.numeros = numeros
        frecuencia = []
        valores_vistos = []
        for numero in self.numeros:
            if numero not in valores_vistos:
                conteo = self.numeros.count(numero)
                frecuencia.append((numero, conteo))
                valores_vistos.append(numero)
        return frecuencia

    def calcular_moda(self):
        mayor_frecuencia = 0
        valores_vistos = []
        valor_moda = 0
        for numero in self.numeros:
            if numero not in valores_vistos:
                conteo = self.numeros.count(numero)
                valores_vistos.append(numero)
                if conteo > mayor_frecuencia:
                    valor_moda = numero
                    mayor_frecuencia = conteo
        return valor_moda

    def mostrar_histograma(self):
        valores_vistos = []
        for numero in self.numeros:
            if numero not in valores_vistos:
                conteo = self.numeros.count(numero)
                valores_vistos.append(numero)
                print(numero, "*" * conteo)

def registrar_cambios(celda, valor):
    global historial_de_cambios
    historial_de_cambios.append((celda, valor))

def deshacer_cambios():
    global historial_de_cambios
    historial_de_cambios.pop(-1)
    print(historial_de_cambios)

def mover_robot_en_almacen(movimientos):
    global almacen

    total_productos = sum(fila.count("P") for fila in almacen)
    productos_recogidos = 0
    x, y = 0, 0

    for movimiento in movimientos:
        if movimiento == "R":
            x += 1
        elif movimiento == "L":
            x -= 1
        elif movimiento == "U":
            y -= 1
        elif movimiento == "D":
            y += 1

        if almacen[y][x] == "#":
            return False
        if almacen[y][x] == "P":
            productos_recogidos += 1
            almacen[y][x] = '.'

    return productos_recogidos == total_productos and (x, y) == (0, 0)

if __name__ == "__main__":
    lista_numeros = [80, 100, 70, 80, 90, 90, 100, 100, 90, 20]
    estadistica = Estadistica()

    resultado_frecuencia = estadistica.calcular_frecuencia(lista_numeros)
    print("Lista con tuplas de la frecuencia\n", resultado_frecuencia, "\n")

    resultado_moda = estadistica.calcular_moda()
    print("La moda es:", resultado_moda, "\n")

    print("Histograma")
    estadistica.mostrar_histograma()
    print()

    historial_de_cambios = []

    while True:
        opcion = int(input("Seleccione la opción que desea hacer\n"
                           "1) Insertar valor a una celda\n"
                           "2) Ver el historial de cambios\n"
                           "3) Deshacer cambios\n"
                           "4) Salir\n"))
        if opcion == 1:
            registrar_cambios(str(input("Ingrese celda en MAYÚSCULAS: ")),
                              float(input("Ingrese un valor: ")))

        elif opcion == 2:
            print(historial_de_cambios, "\n")

        elif opcion == 3:
            deshacer_cambios()

        elif opcion == 4:
            break
        else:
            print("Esa opción no existe")

    print()

    almacen = [
        ['.', '.', '#', 'P'],
        ['.', '#', '.', '.'],
        ['P', '.', 'P', '.'],
        ['#', '.', '#', '.']]

    for fila in almacen:
        print(fila)

    movimientos_robot = ['D', 'D', 'R', 'R', 'U', 'R', 'U', 'D', 'L', 'D', 'L', 'L', 'U', 'U']
    print(mover_robot_en_almacen(movimientos_robot))
