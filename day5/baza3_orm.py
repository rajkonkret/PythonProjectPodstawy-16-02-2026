# Mapowanie obiektowo-relacyjne (ang. Object-Relational Mapping – ORM) – sposób odwzorowania obiektowej
# architektury systemu informatycznego na bazę danych (lub inny element systemu) o relacyjnym charakterze.

# sqlalchemy - orm w pythonie
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# pip install sqlalchemy

# konfiguracja silnika
# echo=True - loguj zdarzenia bazy danych
engine = create_engine("sqlite:///test.db", echo=True)

# deklaracja klasy bazowej
Base = declarative_base()


# model, encja - kalsa odwzororwująca tabelę w bazie danych
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


# tworzenie tabel w bazie danych
Base.metadata.create_all(bind=engine)
# CREATE TABLE users (
# 	id INTEGER NOT NULL,
# 	name VARCHAR,
# 	age INTEGER,
# 	PRIMARY KEY (id)
# )

# tworzenie sesji
Session = sessionmaker(bind=engine)
session = Session()

# dodawanie rekordu
new_user = User(name="Jan", age=30)
session.add(new_user)
session.commit()