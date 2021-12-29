from pymongo import MongoClient
import key
client = key.DB_CLIENT


def get_all(collection, document):
    obj_list = []
    client_db = MongoClient(client)
    data_base = client_db[collection]
    db_document = data_base[document]
    result = db_document.find()
    for obj in result:
        obj_list.append(obj)

    client_db.close()
    return obj_list


def get_one(collection, document, socio_id):
    client_db = MongoClient(client)
    data_base = client_db[collection]
    db_document = data_base[document]
    result = db_document.find_one({"_id": socio_id})
    return result


def update_count(collection, document, socio):
    client_db = MongoClient(client)
    data_base = client_db[collection]
    db_document = data_base[document]
    result = db_document.update_one({"_id": socio["_id"]}, {"$set": socio})
    return result


def create_cobro(result, collection, document):
    client_db = MongoClient(client)
    data_base = client_db[collection]
    document = data_base[document]
    document.insert_one(result)


def deactivate_socio(socio_id):
    client_db = MongoClient(client)
    data_base = client_db["Gym"]
    db_document = data_base["socios"]
    db_document.update_one({"_id": socio_id}, {"$set": {"active": False}})


def realizar_pago(socio_id, update):
    client_db = MongoClient(client)
    data_base = client_db["Gym"]
    db_document = data_base["socios"]
    db_document.update_one({"_id": socio_id}, {"$set": update})
