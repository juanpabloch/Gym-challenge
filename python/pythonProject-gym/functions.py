from mongo import update_count
from datetime import datetime

def descuentosFunction(socio_info, desc_list, plan_list):
    total = 0
    if len(socio_info["descuentos"]) == 0 or type(socio_info["descuentos"]) == str:
        return total

    for des in socio_info["descuentos"]:
        for descuento in desc_list:
            if des["desc_id"] == descuento["_id"] and descuentos_count(des, descuento):
                update_count("Gym", "socios", socio_info)
                if "monto" in descuento:
                    total += descuento["monto"]
                else:
                    total += socio_plan(socio_info, plan_list) * (float(descuento["porcentaje"]) / 100)

    return total


def socio_plan(socio_info, plan_list):
    total = 0
    for plan in plan_list:
        if plan["_id"] == socio_info["plan_id"]:
            total += plan["precio"]

    return total


def total_a_pagar(socio_info, plan_list, desc_list):
    socio_plan_t = socio_plan(socio_info, plan_list)
    socio_desc_t = descuentosFunction(socio_info, desc_list, plan_list)
    if is_socio_vigente(socio_info):
        total = socio_plan_t - socio_desc_t
        if total < 0:
            total = 0
    else:
        return 'socio no vigente'

    return total

#se fija si quedan descuentos por aplicar o no
def descuentos_count(socio_desc, desc):
    if socio_desc["counter"] == desc["aplicaciones"]:
        return False
    else:
        socio_desc["counter"] += 1
        return True


def is_socio_vigente(socio):
    if socio["vigencia"] == datetime.now():
        return False
    else:
        return True


def periodo_cobro():
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    return meses[datetime.now().month - 1]


def cobro_final(desc_list, monto, socio):
    descuentos_final = []
    for desc_in_socio in socio["descuentos"]:
        if len(desc_in_socio) == 0 or type(desc_in_socio) == str:
            descuentos_final = "sin descuentos"
        else:
            for desc_in_list in desc_list:
                if desc_in_list["_id"] == desc_in_socio["desc_id"]:
                    aplic_faltantes = desc_in_list["aplicaciones"] - desc_in_socio["counter"]
                    if aplic_faltantes == 0:
                        descuentos_final = "sin descuentos"
                    else:
                        if "monto" in desc_in_list:
                            descuento_monto = f"${desc_in_list['monto']}"
                        else:
                            descuento_monto = f"{desc_in_list['porcentaje']}%"
                        descuentos_final.append({
                            "id": desc_in_list["_id"],
                            "descuento": descuento_monto,
                            "aplicaciones-restantes": aplic_faltantes
                        })
    cobro = {
        "periodo": periodo_cobro(),
        "monto": f"${monto}",
        "socio_id": socio["_id"],
        "descuentos": descuentos_final
    }
    return cobro
