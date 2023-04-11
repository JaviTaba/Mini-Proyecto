import sqlite3
import uuid

class Database:
    def __init__(self, database_name):
        self.conn = sqlite3.connect(database_name)
        self.cursor = self.conn.cursor()
        self.id_count = 0
    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS user_data (
                user_id INTEGER AUTO_INCREMENT PRIMARY KEY,
                firstname VARCHAR(20) NOT NULL,
                lastname VARCHAR(20) NOT NULL,
                nickname VARCHAR(15),
                age INTEGER NOT NULL,
                email VARCHAR (25) NOT NULL,
                photo VARCHAR(100))''')
        self.conn.commit()
        
    def insert_data(self,firstname,lastname,nickname,age,email,photo):
        self.id_count += 1
        self.cursor.execute("INSERT INTO user_data (user_id, firstname, lastname, nickname, age, email, photo) VALUES (?, ?, ?, ?, ?, ?, ?)",
                          (self.id_count,firstname,lastname,nickname,age,email,photo))
        self.conn.commit()
        
    def buscar_datos(self, nombre):
        self.cursor.execute("SELECT * FROM user_data WHERE nombre=?", (nombre))
        return self.cursor.fetchall()
    
    def cerrar_conexion(self):
        self.conn.close()
