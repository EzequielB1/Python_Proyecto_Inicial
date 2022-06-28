'''
Proyecto Python Inicial
Programa de pedidos de delivery.
---------------------------
Autor: Ezequiel Bianco
Version: 1.1
Descripcion:
Este programa es una simulacion de un programa para cargar pedidos en un local de comidas
y envio a domicilio.
'''

__author__ = "Ezequiel Bianco"
__email__ = "ezequielbianco1102@gmail.com"
__version__ = "1.1" "UPDATE: 28/06/2022"

import csv
import os
import random
os.chdir("C:\\Users\ezeb0\OneDrive\Escritorio\Curso Python INOVE\PYTHON INICIAL\Python Inicial - Proyecto Integrador\Proyecto")


def dias_ofertas():
    """Funcion que nos devuelve la oferta disponible segun el dia de la semana."""
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


def pedido():
    """Esta funcion nos permite hacer pedidos continuamente hasta que indiquemos el final."""
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
                    precios.append(combos["precio"])
                    # Guardamos el pedido en una nueva lista.
            if producto == "fin":
                print("El proceso ha finalizado.")
                break
    print(f"el pedido completo es: {pedidos}")

def forma_pago(como_pago):
    """Funcion que nos permite elegir metodos de pago y nos devuelve las ofertas o recargos disponibles."""
    print("Elija el metodo de pago:",
    "Tarjeta de credito = C,",
    "Debito = D,",
    "Efectivo = E,",
    "MercadoPago = MP")
    como_pago = input("Ingrese forma de pago: ").upper()
    if como_pago == "C":
        print("Con TC los viernes y sabados tenemos un recargo del 5%!")
    elif como_pago == "D":
        print("con TD no tenemos ofertas!")
    elif como_pago == "E":
        print("Pagando en efectivo los sabados y domingos tenemos un 5% de bonificacion")
    elif como_pago == "MP":
        print("Con MercadoPago tenemos un recargo del 10% todos los dias!")
    else:
        print("Ha ingresado una opcion incorrecta!")


def ticket_final():
    """Funcion que imprime el valor total del ticket con los recargos y descuentos realizados."""
    # Iteramos sobre la lista de pedidos, para poder visualizar los precios y obtenemos la suma total.
    suma = 0
    for precio in precios:
        precio = int(precio)
        suma += precio
    print(f"El precio total sin descuentos es: {suma}")
    descuento = int(input("Ingrese el descuento disponible del dia: "))
    recargo = int(input("Ingrese el recargo del dia: "))
    # Condicional que emite ticket segun corresponda con recargo y/o descuento
    if recargo == "0":
        ticket_final = (suma - (descuento * suma) / 100)
        print(f"El precio final del pedido es: ${ticket_final}")
    else:
        precio_recargo = (suma + (recargo * suma) / 100)
        ticket_recargo = (precio_recargo - (descuento * precio_recargo) / 100)
        print(f"El ticket final es: {ticket_recargo}")  



def delivery():
    """El delivery es seleccionado segun un numero aleatorio"""
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
    pedidos = []
    precios = []
    numero_ticket = ""
    como_pago = ""
    dias_ofertas()
    pedido()
    forma_pago(como_pago)
    ticket_final()
    delivery()

