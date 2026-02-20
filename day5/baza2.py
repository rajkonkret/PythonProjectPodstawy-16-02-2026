# baza danych - systemy przechowywania danych
# silnik - mechanizm przecowywania i zarządzania danym
# bazy relacyjne, nierelacyjne
# sql, nosql
# postgress, oracle, mysql, mssql, sqlite

import sqlite3

try:
    conn = sqlite3.connect("baza_danych.db")
    c = conn.cursor()
    print("Baza danych została podłaczona")

    query = """
    CREATE TABLE IF NOT EXISTS developers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    salary REAL NOT NULL
    );
    """
    c.execute(query)
    conn.commit()

    # insert
    insert = "INSERT INTO developers (id,name,email,salary) VALUES (1,'Radek','raj@raj.pl', 10000);"
    # c.execute(insert) # komentowane by nie wpisywać do bazy tych samych danych
    # conn.commit()

    insert = "INSERT INTO developers (id,name,email,salary) VALUES (2,'Radek','raj1@raj.pl', 8000);"
    # c.execute(insert)
    # conn.commit()

    select = "SELECT * FROM developers;"
    for row in c.execute(select):
        print(row)  # (1, 'Radek', 'raj@raj.pl', 10000.0)

    update = """
    UPDATE developers SET salary=11000 WHERE id=1;
    """
    c.execute(update)
    conn.commit()

    delete = """
    DELETE FROM developers WHERE id=1;
    """
    c.execute(delete)
    conn.commit()
    # Baza danych została podłaczona
    # (2, 'Radek', 'raj1@raj.pl', 8000.0)
    # Połączenie zostało zamknięte

except sqlite3.Error as e:
    print("Bład podłaczenia bazy danych:", e)
finally:
    if conn:
        conn.close()
        print("Połączenie zostało zamknięte")
# pgadmin, dbeaver, https://sqlitebrowser.org/, TablePlus
# SimpleSqliteBrowser
# Baza danych została podłaczona
# Połączenie zostało zamknięte
