import mongo
import schedule
import time
from datetime import date
from functions import gym_cobros

def cobros():
    socios_list = mongo.get_all("Gym", "socios")
    planes_list = mongo.get_all("Gym", "planes")
    descuentos_list = mongo.get_all("Gym", "descuentos")

    if date.today().day != 30:
        return
    for socio in socios_list:
        gym_cobros(socio, planes_list, descuentos_list)
    print(" ")
    print("----------------New period---------------")




def scheduler():
    print("starting Gym program")
    schedule.every(1).day.at("10:00").do(cobros)
    # schedule.every(30).seconds.do(cobros)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    scheduler()

