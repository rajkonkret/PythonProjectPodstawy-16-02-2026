# Mapowanie obiektowo-relacyjne (ang. Object-Relational Mapping – ORM) – sposób odwzorowania obiektowej
# architektury systemu informatycznego na bazę danych (lub inny element systemu) o relacyjnym charakterze.

# sqlalchemy - orm w pythonie
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
# pip install sqlalchemy