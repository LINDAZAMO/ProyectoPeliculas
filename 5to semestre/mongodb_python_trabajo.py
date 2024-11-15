from pymongo import MongoClient


client = MongoClient("localhost:27017")

db = client["ClinicaDental"]

collection = ["paciente", "dentista", "costo", "cita", "consultorios", "procedimiento"]

document = {}

for tabla in collection:
    reslutado = db[tabla].find()
    print()
    print(tabla)
    for i in reslutado:
        print(i)
        