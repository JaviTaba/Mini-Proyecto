import os,time
from Database.dbdemo import Database

print("----------------BOT JAVI----------------")
print("Hola! Soy la primer version del Javi Virtual hecho con IA.\nA continuacion te pedire informacion para crear mi base de datos con toda tu info.")
firstname = input("Ingresa tu primer nombre: ")
lastname = input("Ingresa tu apellido: ")
nickname = input("Si tienes algun apodo, ingresalo. Si no, deja el espacio en blanco: ")
age = int(input("Ingresa tu edad: "))
email = input("Por favor, ingresa tu email: ")
photo = input("Ingresa el URL de una foto tuya: ")
os.system('cls')
print("------------RECOPILANDO INFORMACION-----------------")
db = Database('demodatabase.db')
db.create_table()
db.insert_data(firstname,lastname,nickname,age,email,photo)
total_items = 100

# Loop que simula el progreso de una tarea
for i in range(total_items):
    # Cálculo del porcentaje de progreso
    progress_pct = (i + 1) / total_items * 100

    # Impresión de la barra de progreso
    progress_bar = '[' + '#' * int(progress_pct // 10) + ' ' * (10 - int(progress_pct // 10)) + ']'
    print('\r' + progress_bar + f' {progress_pct:.2f}%', end='')

    # Simulación de una tarea que toma un tiempo
    time.sleep(0.01)

# Impresión final de la barra de progreso completa
print('\r' + '[' + '#' * 10 + '] 100.00%')
