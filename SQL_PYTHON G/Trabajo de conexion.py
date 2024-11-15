import mysql.connector
from mysql.connector import connect,

def consultar_base_datos():
    try:
        #acceder a la base
        conexion = connect(host="localhost", port="3306", user="root",
                           password="12345678", database="escuela")
        cursor = conexion.cursor()
        sql = "Select * from alumnos"


        cursor.execute(sql)
        lista = cursor.fetchall()

        for result in cursor.stored_results():
            rows = result.fetchall()
            for row in rows:
                print(row)

        cursor.close()
        conexion.close()
excep mysql.connector

        print(conexion)
    except Error as e:
        print(e)
print(e)