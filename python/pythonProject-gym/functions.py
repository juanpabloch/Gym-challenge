from mongo import update_count
from mongo import deactivate_socio
from mongo import create_cobro
from datetime import datetime


def is_socio_vigente(socio):
    if socio["vigencia"] < datetime.now():
        deactivate_socio(socio['_id'])
        return False
    else:
        return True


def descuentos_total_socio(socio_info, desc_list, plan_list):
    total = 0
    if not socio_info["active"]:
        return total

    if len(socio_info["descuentos"]) == 0 or type(socio_info["descuentos"]) == str:
        return total

    for des in socio_info["descuentos"]:
        for descuento in desc_list:
            if des["desc_id"] == descuento["_id"] and descuentos_count(des, descuento):
                if "monto" in descuento:
                    total += descuento["monto"]
                else:
                    total += socio_plan_monto(socio_info, plan_list) * (float(descuento["porcentaje"]) / 100)

    return total


def descuentos_count(socio_desc, desc):
    if socio_desc["counter"] == desc["aplicaciones"]:
        return False
    else:
        return True


def socio_plan_monto(socio_info, plan_list):
    total = 0
    for plan in plan_list:
        if plan["_id"] == socio_info["plan_id"]:
            total += plan["precio"]

    return total


def total_a_pagar(socio_info, plan_list, desc_list):
    if socio_info["active"]:
        socio_plan_t = socio_plan_monto(socio_info, plan_list)
        socio_desc_t = descuentos_total_socio(socio_info, desc_list, plan_list)
        total = socio_plan_t - socio_desc_t
        if total < 0:
            total = 0
        return float(total)
    else:
        return 'socio no vigente'


def periodo_cobro():
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    return meses[datetime.now().month - 1]


def cobro_periodo(socio, monto, desc_list):
    descuentos_final = []
    if type(socio["descuentos"]) == str:
        descuentos_final = "sin descuentos"
    else:
        for desc_in_socio in socio["descuentos"]:
            for desc_in_list in desc_list:
                if desc_in_socio["desc_id"] == desc_in_list["_id"]:
                    aplic_faltantes = desc_in_list["aplicaciones"] - desc_in_socio["counter"]
                    if aplic_faltantes > 0:
                        desc_in_socio["counter"] += 1
                        update_count("Gym", "socios", socio)
                        if "monto" in desc_in_list:
                            descuento_monto = f"${desc_in_list['monto']}"
                        else:
                            descuento_monto = f"{desc_in_list['porcentaje']}%"

                        descuentos_final.append({
                            "id": desc_in_list["_id"],
                            "descuento": descuento_monto,
                            "aplicaciones-restantes": aplic_faltantes - 1
                        })

    if len(descuentos_final) == 0:
        descuentos_final = "sin descuentos"
    cobro = {
        "socio_id": socio["_id"],
        "periodo": periodo_cobro(),
        "monto": f"${monto}",
        "descuentos": descuentos_final
    }
    print(cobro)
    create_cobro(cobro, "Gym", "pagos")


def cobro_no_vigente(socio):
    cobro = {
        "socio_id": socio["_id"],
        "periodo": periodo_cobro(),
        "monto": "Socio no vigente"
    }
    print(cobro)


def gym_cobros(socio_info, plan_list, desc_list):
    if is_socio_vigente(socio_info):
        monto_a_pagar = total_a_pagar(socio_info, plan_list, desc_list)
        cobro_periodo(socio_info, monto_a_pagar, desc_list)
    else:
        cobro_no_vigente(socio_info)
