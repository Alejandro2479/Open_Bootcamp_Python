import sqlite3

conn = sqlite3.connect('alumnos.db')

conn.execute('''CREATE TABLE Alumnos
             (id INT PRIMARY KEY NOT NULL,
             nombre TEXT NOT NULL,
             apellido TEXT NOT NULL);''')

conn.execute("INSERT INTO Alumnos (id,nombre,apellido) VALUES (1, 'Juan', 'Pérez')")
conn.execute("INSERT INTO Alumnos (id,nombre,apellido) VALUES (2, 'María', 'García')")
conn.execute("INSERT INTO Alumnos (id,nombre,apellido) VALUES (3, 'Pedro', 'Sánchez')")
conn.execute("INSERT INTO Alumnos (id,nombre,apellido) VALUES (4, 'Ana', 'Martínez')")
conn.execute("INSERT INTO Alumnos (id,nombre,apellido) VALUES (5, 'Miguel', 'López')")
conn.execute("INSERT INTO Alumnos (id,nombre,apellido) VALUES (6, 'Lucía', 'Fernández')")
conn.execute("INSERT INTO Alumnos (id,nombre,apellido) VALUES (7, 'Javier', 'Gómez')")
conn.execute("INSERT INTO Alumnos (id,nombre,apellido) VALUES (8, 'Sofía', 'Ruiz')")

# Guardamos los cambios
conn.commit()

cursor = conn.execute("SELECT * FROM Alumnos WHERE nombre='Juan'")
for row in cursor:
    print("ID = ", row[0])
    print("Nombre = ", row[1])
    print("Apellido = ", row[2], "\n")
    
conn.close()
