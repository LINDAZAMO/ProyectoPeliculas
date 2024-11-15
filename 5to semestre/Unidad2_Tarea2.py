#Linda Jaqueline Vazquez Zamora
#951
#04/11/2024
from mysql.connector import connect, Error
class MySQLConnect:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conexion = None
        self.cursor = None

    def conectar(self):
        try:
            self.conexion = connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.conexion.cursor()
            print("Conectado a la base de datos")
        except Error as b:
            print("Error al conectar:", b)

    def desconectar(self):
        if self.conexion:
            self.cursor.close()
            self.conexion.close()
            print("Se desconecto correctamente de la base de datos.")


class PaisMySQL(MySQLConnect):
    def insertar(self, id, nombre):
        try:
            sql = "insert into Pais (id, nombre) values (%s, %s)"
            valores = (id, nombre)
            self.cursor.execute(sql, valores)
            self.conexion.commit()
            print("País insertado")
            return True
        except Error as b:
            print("Error al insertar:", b)
            return False

    def editar(self, id, nombre):
        try:
            sql = "update Pais set nombre = %s where id = %s"
            valores = (nombre, id)
            self.cursor.execute(sql, valores)
            self.conexion.commit()
            print("País actualizado")
        except Error as b:
            print("Error al actualizar:", b)

    def eliminar(self, id):
        try:
            sql = "delete from Pais where id = %s"
            self.cursor.execute(sql, (id,))
            self.conexion.commit()
            print("País eliminado correctamente.")
            return True
        except Error as b:
            print("Error al eliminar:", b)
            return False

    def consultar(self, filtro):
        try:
            sql = f"select * from Pais where {filtro}"
            self.cursor.execute(sql)
            resultados = self.cursor.fetchall()
            return resultados
        except Error as b:
            print("Error al consultar:", b)
            return []


class OlimpiadaMySQL(MySQLConnect):
    def insertar(self, id, year):
        try:
            sql = "insert into Olimpiada (id, year_olimpiada) values (%s, %s)"
            valores = (id, year)
            self.cursor.execute(sql, valores)
            self.conexion.commit()
            print("Olimpiada insertada")
            return True
        except Error as b:
            print("Error al insertar:", b)
            return False

    def editar(self, id, year):
        try:
            sql = "update Olimpiada set year_olimpiada = %s where id = %s"
            valores = (year, id)
            self.cursor.execute(sql, valores)
            self.conexion.commit()
            print("Año de Olimpiada actualizado")
        except Error as b:
            print("Error al actualizar:", b)

    def eliminar(self, id):
        try:
            sql = "delete from Olimpiada where id = %s"
            self.cursor.execute(sql, (id,))
            self.conexion.commit()
            print("Olimpiada eliminada")
            return True
        except Error as b:
            print("Error al eliminar:", b)
            return False

    def consultar(self, filtro):
        try:
            sql = f"select * from Olimpiada where {filtro}"
            self.cursor.execute(sql)
            resultados = self.cursor.fetchall()
            return resultados
        except Error as b:
            print("Error al consultar:", b)
            return []


if __name__ == "__main__":
    db = PaisMySQL("localhost", "root", "12345678", "olimpiadas")
    db.conectar()

    db.insertar(1, "México")
    db.editar(1, "Perú")
    print(db.consultar("id = 1"))

    db.eliminar(1)
    db.desconectar()