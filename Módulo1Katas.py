# program.py
from datetime import date
import calendar
curr_date = date.today()
print(calendar.day_name[curr_date.weekday()])
from datetime import date
print("Today's date is: " + str(date.today()))
print("Bienvenido a la Cálculadora de Conversión : Parsec a Lightyears")
name = input("Introduzca su nombre de tripulante: ")
print("Saludos: " + name)
#Conversión de Parsec a Lightyears
print("Conversión de Parsec a Lightyears")
#Conversión Fase Cálculo de Parsec a Lightyears
print("Iniciando Sistema")
parsec = int (input("Introduzca las unidades de Parsec: "))
lightyears = 3.26156 * parsec
print(str(parsec) + " Parsec, es o son " + str(lightyears) + " Lightyears")
#KND
print("Fin de la Operación")
name = input("Introduzca el código de su nueva: ")
print("Accesando a la base de datos de KND")
print("Codename: Kids Next Door")
print("Code: MOON")