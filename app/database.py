import sqlite3


def get_db():
    connection = sqlite3.connect("memora_al.db")
    connection.row_factory = sqlite3.Row
    return connection


def init_db(app):
    with app.app_context():
        connection = get_db()

        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS leads (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                isim TEXT NOT NULL,
                telefon TEXT NOT NULL,
                mesaj TEXT,
                tarih TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

        connection.commit()
        connection.close()


def lead_ekle(isim, telefon, mesaj=None):
    connection = get_db()

    connection.execute(
        "INSERT INTO leads (isim, telefon, mesaj) VALUES (?, ?, ?)",
        (isim, telefon, mesaj)
    )

    connection.commit()
    connection.close()


def tum_leadler():
    connection = get_db()

    rows = connection.execute(
        "SELECT * FROM leads ORDER BY tarih DESC"
    ).fetchall()

    connection.close()

    return [dict(row) for row in rows]