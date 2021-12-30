from mongo import realizar_pago
from datetime import datetime
from datetime import timedelta

update = {
    "vigencia": datetime.now() + timedelta(minutes=2),
    "active": True
}

print("pagando")
realizar_pago(1, update)
realizar_pago(2, update)
realizar_pago(3, update)
print("fin")
