import fun as ff
from os import system as ss

op = 0

empleados = ["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]


while op !=5:
    ss("cls")
    ff.menu()
    op = ff.validar_op()
    if  op==1:
        ss("cls")
        ff.generar_sueldos(empleados)
        ss("pause")
    elif op==2:
        ss("cls")
        ff.clasificar_sueldos(empleados)
        ss("pause")
    elif op==3:
        ss("cls")
        ff.imprimir_estadisticas(empleados)
        ss("pause")
    elif op==4:
        ss("cls")
        ff.report_sueldos(empleados)
        ss("pause")

ss("cls")
print("se esta cerrando el programa....")
print("Creador: matias vega")
print("rut: 22 004 215-4 ")