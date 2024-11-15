
from mysql.connector import connect, Error
def consultar_base_datos():
    try:
        #acceder a la base
        conexion = connect(host="localhost", port="3306", user="root",
                           password="12345678", database="escuela")
        cursor = conexion.cursor()
        #comando
        sql = "Select * from alumnos"
        #ejecuta el comando
        cursor.execute(sql)
        #extraer los datos de la entidad
        lista = cursor.fetchall()
        for item in lista:
            print(item)
            #tambien se puede hacer print(item[1], "-----", item[2]) para extraer los datos que quieras empezando de 0



        print(conexion)
    except Error as e:
        print(e)

def insertar_base_datos():
    try:
        conexion = connect(host="localhost", port="3306", user="root",
                           password="12345678", database="escuela")
        cursor = conexion.cursor()
        sql = "INSERT INTO CARRERA( id, nombre_carrera, descripcion, id_materia, id_alumnos, id_profesor, id_grupo) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        # el comando sig es para evitar un hacking y se ponen los datos que ingreses aqui a la entidad carrera
        s = (102, "prueba2", "pruebas insertar", 2, 4, 6, 8)
        cursor.execute(sql, s)

        #elcommint es para que se reflejen los datosen la base de datos
        conexion.commit()

        print(cursor.lastrowid)
        print(cursor.rowcount)

        #importante
        cursor.close()
        conexion.close()
    except Error as e:
        print(e)


def insertar_valores():
    try:
        conexion = connect(host="localhost", port="3306", user="root",
                           password="12345678", database="escuela",
                           auth_plugin= 'mysql_native_password')
        cursor = conexion.cursor()
        sql = "INSERT INTO CARRERA( id, nombre_carrera, descripcion, id_materia, id_alumnos, id_profesor, id_grupo) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        # el comando sig es para evitar un hacking y se ponen los datos que ingreses aqui a la entidad carrera
        s  = [(104,"prueba4","Pruebas insertar4",3, 4, 3, 2),
                   (105, "prueba5", "Pruebas insertar5", 3, 4, 4, 4),
                   (106, "prueba6", "Pruebas insertar6", 3, 4, 6, 8,),
                   (107, "prueba7", "Pruebas insertar7", 3, 4, 5, 3),
                   ]
        cursor.executemany(sql, s)
        conexion.commit()
        print(cursor.rowcount)
        cursor.close()
        conexion.close()
    except Error as e:
        print(e)

if __name__  == "__main__":
    consultar_base_datos()
    insertar_base_datos()
    insertar_valores()