# Challenge GYM

---

Se debe crear un proceso de cobros recurrentes para una cadena de gimnasios que posee
varios socios, y varios planes de suscripción con precios diferentes. El proceso identifica los
socios a los que se les debe cobrar según la fecha y el estado.

### Installation:

debemos utilizar [pip](https://pip.pypa.io/en/stable/) para instalar las librerias que vamos a utilizar.

```bash
pip install pymongo
```
PyMongo contiene herramientas para trabajar con MongoDB y es la forma recomendada de trabajar con MongoDB desde Python. [PyMongo](https://pymongo.readthedocs.io/en/stable/)

```bash
pip install "pymongo[srv]"
```
Soporte para mongodb+srv:// URIs (necesita dnspython)
```bash
pip install schedule
```
Ejecuta funciones de Python (o cualquier otra funcion) periódicamente. Se utiliza para ejecutar el codigo principal. [Schedule](https://schedule.readthedocs.io/en/stable/)

### Seeders:
Podemos cargar la nuestra base de datos con el comando:
```bash
>> python seeder.py 
```

### Key file:
debemos crear un archivo key.py el cual debe contener:
* DB_PASSWORD = corresponde a la password de nuestra base de datos
* DB_CLIENT = es la direccion de la base de datos o connection string

## Comenzar App

---
para comenzar ejecutamos en la consola:
```bash
>> python main.py 
```

### simular un pago:
Para recetear al socio o simular un pago podemos correr el archivo:
```bash
>> python simulador_pagos.py 
```

---

Gracias!

_creado por:_  **Choternasty Juan Pablo**
