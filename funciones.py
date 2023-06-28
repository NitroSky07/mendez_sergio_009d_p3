import time
import msvcrt
import os
import numpy as  np


def ver_guarderia():
    while True:
        np.zeros(1,2)
        for x in range(2):
            print("\tFila", end=" ")
            for y in range(5):
                print("Columna", end=" ")
                
def ver_menu():
    os.system('cls')
    while True:
        print("""MENÚ
        1.Ver guardería
        2.Grabar (Registrar datos del dueño y datos de la mascota)
        3.Buscar datos de la mascota
        4.Retirarse(Monto a pagar)
        5.Salir""")
        print(input("Ingrese opcion: "))
        
def validar_opcion():
    while True:
        try:
            opc = int(input("Ingrese opción: "))
            if opc in(1,2,3,4,5):
                return opc
            else:
                print("ERROR! OPCIÓN INCORRECTA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO!")

def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese rut: "))
            if rut >= 1000000 and rut <= 99999999:
                return rut
            else:
                print("ERROR! RUT ENTRE 1000000 Y 99999999!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

lista_ruts=[]
lista_nombresd=[]
lista_nombresm=[]

def validar_nombre():
    while True:
        nom = input("Ingrese nombre: ")
        if len(nom.strip()) >= 3 and nom.isalpha():
            return nom
        else:
            print("ERROR! DEBE TENER AL MENOS 3 LETRAS!")
        
        while True:
            nom_mas = input("Ingrese nombre de su mascota: ")
            if len(nom_mas.strip()) >= 3 and nom_mas.isalpha():
                return nom_mas
            else:
                print("ERROR! DEBE TENER AL MENOS 3 LETRAS!")

def validar_fila():
    while True:
        try:
            fila = int(input("Ingrese número fila(1-2): "))
            if fila >= 1 and fila <= 2:
                return fila
            else:
                print("ERROR! FILA INCORRECTA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def validar_columna():
    while True:
        try:
            columna = int(input("Ingrese número columna(1-5): "))
            if columna >= 1 and columna <= 5:
                return columna
            else:
                print("ERROR! COLUMNA INCORRECTA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")