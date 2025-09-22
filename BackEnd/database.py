import mysql.connector

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "GeoGlub"
}

def create_tables():
    conn = mysql.connector.connect(**DB_CONFIG)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS bar (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(255) UNIQUE NOT NULL,
        terraza BOOLEAN DEFAULT 0,
        tiene_tele BOOLEAN DEFAULT 0,
        comentario TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS cerveza (
        id INT AUTO_INCREMENT PRIMARY KEY,
        marca VARCHAR(255) NOT NULL,
        precio FLOAT NOT NULL,
        bar_id INT,
        FOREIGN KEY(bar_id) REFERENCES bar(id)
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS juego (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(255) UNIQUE NOT NULL
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS bar_juego (
        bar_id INT,
        juego_id INT,
        PRIMARY KEY (bar_id, juego_id),
        FOREIGN KEY(bar_id) REFERENCES bar(id),
        FOREIGN KEY(juego_id) REFERENCES juego(id)
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS usuario (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(255) NOT NULL,
        apellido VARCHAR(255) NOT NULL,
        edad INT
    )
    """)

    conn.commit()
    cur.close()
    conn.close()

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)

if __name__ == "__main__":
    create_tables()