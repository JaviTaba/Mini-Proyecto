import sqlite3

# Crear clase Database

#metodo para crear todas las tablas

#metodo para insertar datos en cada tabla
##recibe argumentos 

conn =  sqlite3.connect('database.db')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS user_data (
                user_id INTEGER AUTO_INCREMENT PRIMARY KEY,
                firstname VARCHAR(20) NOT NULL,
                lastname VARCHAR(20) NOT NULL,
                nickname VARCHAR(15),
                age INTEGER NOT NULL,
                email VARCHAR (25) NOT NULL,
                photo VARCHAR(100)
                ) ''')

cursor.execute("INSERT INTO user_data VALUES(2,'Lautaro','Pozzo','Lauti', 25, 'lautaropozzo@hotmail.com', 'https://drive.google.com/file/d/10-DWwr6NG1PiXT4Z4F_9PEB2cbzPkYxe/view?usp=share_link')")

cursor.connection.commit()
cursor.connection.close()