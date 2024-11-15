from mysql.connector import Error
import mysql.connector
from pymongo import MongoClient


mysql_config = {
    'host': "localhost",
    'database': "hamburguesas",
    'user': "root",
    'password': "12345678"
}
mongo_client = MongoClient("127.0.0.1:27017")
mongo_db = mongo_client["hamburguesas"]
mongo_collection = mongo_db["tipos_hamburguesas"]

try:
    mysql_conn = mysql.connector.connect(**mysql_config)
    if mysql_conn.is_connected():
        print("Conexión exitosa a MySQL")
        cursor = mysql_conn.cursor(dictionary=True)
        cursor.execute("select * from tipos_hamburguesas")
        tipos_hamburguesas_data = cursor.fetchall()
        if tipos_hamburguesas_data:
            mongo_collection.insert_many(tipos_hamburguesas_data)
            print("Datos migrados a MongoDB")
        else:
            print("No se hay datos en la tabla 'tipos_hamburguesas' de MySQL")


except Error as e:
    print("Error al conectar a MySQL:", e)

finally:
    if mysql_conn.is_connected():
        cursor.close()
        mysql_conn.close()
        print("Conexión a MySQL cerrada")