from pymongo import MongoClient
from datetime import datetime
from datetime import timedelta

client = 'mongodb+srv://juanpabloch:asd567jkl123@cluster0.mxijk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'

client_migration = MongoClient(client)
db = client_migration["Gym"] #collection
descuentos = db["descuentos"] #document
planes = db["planes"] #document
socios = db["socios"] #document


planes_list = [
    {
        "_id": 1,
        "name": "plan a",
        "precio": 100
    },
    {
        "_id": 2,
        "name": "plan b",
        "precio": 150
    },
    {
        "_id": 3,
        "name": "plan c",
        "precio": 170
    }
]
planes.insert_many(planes_list)

descuentos_list = [
    {
        "_id": 1,
        "porcentaje": 50,
        "aplicaciones": 12
    },
    {
        "_id": 2,
        "monto": 30,
        "aplicaciones": 6
    },
    {
        "_id": 3,
        "porcentaje": 10,
        "aplicaciones": 3
    }
]
descuentos.insert_many(descuentos_list)

socios_list = [
    {
        "_id": 1,
        "plan_id": 1,
        "descuentos": [
            {
                "desc_id": 1,
                "counter": 0
            },
            {
                "desc_id": 2,
                "counter": 0
            }
        ],
        "vigencia": datetime.now() + timedelta(days=30),
        "active": True
    },
    {
        "_id": 2,
        "plan_id": 2,
        "descuentos": [
            {
                "desc_id": 2,
                "counter": 0
            }
        ],
        "vigencia": datetime.now() + timedelta(days=30),
        "active": True
    },
    {
        "_id": 3,
        "plan_id": 3,
        "descuentos": "null",
        "vigencia": datetime.now() + timedelta(days=30),
        "active": True
    }
]

socios.insert_many(socios_list)
