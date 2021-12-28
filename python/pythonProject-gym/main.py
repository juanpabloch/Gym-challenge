import mongo
import schedule
import time
from datetime import date
from functions import total_a_pagar
from functions import cobro_final
from mongo import create_cobro

socios_list = mongo.get_all("Gym", "socios")
planes_list = mongo.get_all("Gym", "planes")
descuentos_list = mongo.get_all("Gym", "descuentos")


def info():
    if date.today().day != 30:
        return
    for socio in socios_list:
        a_pagar = total_a_pagar(socio, planes_list, descuentos_list)
        result = cobro_final(descuentos_list, a_pagar, socio)
        print(result)
        create_cobro(result, "Gym", "pagos")


schedule.every().day.at("10:00").do(info)


def scheduler():
    print("starting scheduler")
    schedule.every(5).seconds.do(info)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    # info()
    scheduler()

