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