# programa para convertir monedas

from ast import parse
import string


montoSoles = float(input("ingrese el monto en soles : "))

montoDolares = montoSoles * 3.80

print("El monto en dolares es :" + str(montoDolares))