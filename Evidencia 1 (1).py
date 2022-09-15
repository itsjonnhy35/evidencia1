#Proceso para reservar una sala
import random
import datetime
import time

sala = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Salas disponibles: " , sala)

turnos = ['Matutino, Vespertino, Nocturno']

print("Los turnos son: " , turnos)

eventos = ['Programacion en Python, Lenguaje en SQL, Ciberseguridad, Habilidades en programacion, Cursos en Python, Cursos de base de datos, Mundo Cibernetico, Cisco Networking Academy, Introduccion a la programacion, Programacion avanzada']

print("Los eventos son: " , eventos)

print("Los eventos se deben realizar con dos dias de anticipacion")

fecha_actual = datetime.date.today()
print(f"La fecha es {fecha_actual}")



cliente = (input("¿Es usted un cliente registrado?: "))
if cliente == 'Si':
    sala = input("Sala que desea reservar:")
    turno = input("Turno que desea reservar:")
    evento = input("Evento que desea ingresar:")
    print(f"Su sala es {sala}, el turno asignado es {turno}, el evento sera {evento}")

else:
    print("Debe registrarse primero")
    nombre = (input("Ingrese su Nombre: "))

    datos = (input("Ingrese su primer apellido: "))

    numerorandom = random.randrange(100)
    letrarandom = random.randrange(500)
    segundo_numerorandom = random.randrange(100)

    clave = numerorandom + letrarandom
    print(f"Su clave unica es: ", clave)

    print(type(clave))
    print(clave)

    clave_buena = nombre.lower()[0:2] + str(clave) + datos.lower()[0:2] + str(segundo_numerorandom)
    print(clave_buena)

    print("Registro completo, puede reservar su sala")
    sala = input("Sala que desea reservar:")
    turno = input("Turno que desea reservar:")
    print(f"Su sala es {sala} y el turno asignado es {turno}")
    
print("Se le asignara la clave de la sala")

lista = []

for _ in range(10):
    lista.append("s" + str(random.randrange(1,500)))
    
#print(lista)
    
clave_sala1 = lista[0]
clave_sala2 = lista[1]
clave_sala3 = lista[2]
clave_sala4 = lista[3]
clave_sala5 = lista[4]
clave_sala6 = lista[5]
clave_sala7 = lista[6]
clave_sala8 = lista[7]
clave_sala9 = lista[8]
clave_sala10 = lista[9]

print(clave_sala5)


if len(lista) == len(set(lista)):
    print("Se genero la clave con exito")
else:
    print("Hay una clave repetida")
    
print("Se agregara el nombre, la clave y el telefono para el cliente en una lista")

lista = ['Nombre', 'Clave', 'Telefono']

nombre = (input("Dime tu nombre:"))
clave = (input("Dame tu clave de usuario:"))
telefono = (input("Dame tu telefono:"))

lista[0] = nombre
lista[1] = clave
lista[2] = telefono

print(lista)

print("Ahora se agregara la clave de la sala, el numero de la sala y el evento de la sala")

lista1 = ['Clave', 'Numero', 'Evento']

clave1 = (input("Dime la clave de la sala:"))
numero1 = (input("Dime el numero de la sala:"))
evento1 = (input("Dime el nombre del evento:"))

lista1[0] = clave1
lista1[1] = numero1
lista1[2] = evento1

print(lista1)

print("La lista de todos los datos es:")

todos_los_datos = lista + lista1

print(todos_los_datos)


# fecha_capturada = (input("Dime la fecha que deseas reservar con este formato dd/mm/aaaa:"))
# 
# fecha_procesada = datetime.datetime.strptime(fecha_capturada, "%d/%m/%Y").date()

# print(f"la fecha que estas solicitando es: {fecha_procesada}")


fecha_actual = datetime.date.today()
procede = 0

while procede == 0:
    fecha_capturada = (input("Dime la fecha que deseas reservar con este formato dd/mm/aaaa:"))

    fecha_procesada = datetime.datetime.strptime(fecha_capturada, "%d/%m/%Y").date()

    print(f"la fecha que estas solicitando es: {fecha_procesada}")

    cant_dias = 2
    nueva_fecha = fecha_procesada + datetime.timedelta(days=-cant_dias)


    if fecha_actual < nueva_fecha:
        print("su registro se completara con exito")
        print(f"Su fecha se confirma registrada para, {fecha_procesada}")
        procede = procede + 1
    else:
        print("La fecha no respeta el requisito de reservacion de no mayor a 2 dias")
        
todos_los_datos.append(fecha_procesada)

print("Los datos obtenidos finalmente son los siguientes")
print("Nombre Cliente...Clave Cliente...Telefono...Clave Sala...Num.Sala...NombreEvento...fecha")
print(todos_los_datos)

print("Registro Completado")

modificar = input("Desea modificar el nombre de su evento? 1 = SI, 2 = NO: ")

if modificar == 1:
    todos_los_datos[5] = int("Ingrese el nombre que desea")
    print(todos_los_datos)
else:
    print("Fin del registro")
    
    

        













    






    













