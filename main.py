import csv
import os
import random

os.chdir("C:\\Users\ezeb0\OneDrive\Escritorio\Curso Python INOVE\PYTHON INICIAL\Python Inicial - Proyecto Integrador\Proyecto")

'''
Proyecto Python Inicial
Programa de pedidos de delivery.
---------------------------
Autor: Ezequiel Bianco
Version: 1.0

Descripcion:
Este programa es una simulacion de un programa para cargar pedidos en un local de comidas
y envio a domicilio.
'''

__author__ = "Ezequiel Bianco"
__email__ = "ezequielbianco1102@gmail.com"
__version__ = "1.0"


def dias_ofertas():
    dia = input("Ingrese un dia: ")
    # Abrimos el csv con las ofertas y guardamos en variable data
    with open('ofertas.csv', "r") as ofertas_file:
        data = list(csv.DictReader(ofertas_file))
        # Iteramos y seleccionamos la opcion segun el input ingresado
        for dias in data:
            if dias["dias"] == dia and dia != "lunes":
                print("los dias", dias["dias"], "tenemos un:", dias["oferta"], "de descuento")
        if dia == "lunes":
            print(f"Los {dia} estamos cerrados!")

pedidos = []
def pedido():
    # Un ciclo while para poder seleccionar mas de un combo.
    while True:
        producto = input("Ingrese un combo: ")
        with open("combos.csv", "r") as combos_file:
            data = csv.DictReader(combos_file)
            # Leemos el CSV e iteramos para seleccionar el combo
            for combos in data:
                if combos["combos"] == producto:
                    print(combos["producto"])
                    pedidos.append(combos["producto"])
                    pedidos.append(combos["precio"])
                    # Guardamos el pedido en una nueva lista.
            if producto == "fin":
                print("El proceso ha finalizado.")
                break
    print(f"el pedido completo es: {pedidos}")

def forma_pago(como_pago):
    print("Elija el metodo de pago:",
    "Tarjeta de credito = C,",
    "Debito = D,",
    "Efectivo = E,")
    como_pago = input("Ingrese forma de pago: ").upper()
    if como_pago == "C":
        print("Con TC los viernes y sabados tenemos un recargo del 5%!")
    elif como_pago == "D":
        print("con TD no tenemos ofertas!")
    elif como_pago == "E":
        print("Pagando en efectivo los sabados y domingos tenemos un 5% de bonificacion")
    else:
        print("Ha ingresado una opcion incorrecta!")


def ticket_final():
    # Iteramos sobre la lista de pedidos, para poder visualizar los precios
    for pedido in pedidos:
        if len(pedido) < 6:
            print(pedido)
    precio_pedido = int(input("Ingrese el precio total del pedido: "))
    precio_descuento = int(input("Ingrese el descuento disponible del dia: "))
    precio_final = (precio_pedido - (precio_descuento * precio_pedido) / 100)
    # La variable precio_final nos tira el precio con el descuento ya realizado.
    print(f"El precio final del pedido es: ${precio_final}")

def delivery():
    numero_ticket = random.randrange(100)
    print(f"Su numero de ticket es: {numero_ticket}")
    if numero_ticket >= 0 and numero_ticket <= 25:
        print("Su repartidor es: Ezequiel")
    elif numero_ticket > 25 and numero_ticket <= 50:
        print("Su repartidor es: Javier")
    elif numero_ticket > 50 and numero_ticket <= 75:
        print("Su repartidor es: Aldana")
    elif numero_ticket > 75 and numero_ticket <= 100:
        print("Su repartidor es: Eugenia")

            
if __name__ == '__main__':
    print("Bienvenidos al programa para cargar pedidos de BurguerPy")
    numero_ticket = ""
    como_pago = ""
    dias_ofertas()
    pedido()
    forma_pago(como_pago)
    ticket_final()
    delivery()