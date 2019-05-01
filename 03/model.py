from pony.orm import Database, PrimaryKey, Required, Set, db_session, Optional
from uuid import uuid4 as gid, UUID
import datetime as dt
import os


db = Database()

# ukoliko želiš da se svaki puta briše baza
# if os.path.exists("database.sqlite"):
#    os.remove("database.sqlite")

db.bind(provider='sqlite', filename='database.sqlite', create_db=True)


class Student(db.Entity):
    id = PrimaryKey(str)
    jmbag = Required(str)
    ime = Required(str)
    # Veza na više, pišemo kao string jer je definirano tek niže
    kolegiji = Set("Kolegij")
    ocjene = Set("StavkaIspita")


class Kolegij(db.Entity):
    id = PrimaryKey(str)
    naziv = Required(str)
    semestar = Required(int)
    # Veza na više, ovaj puta ne mora kao string, ali može
    studenti = Set(Student)
    ispiti = Set("Ispit")


class Ispit(db.Entity):
    id = PrimaryKey(str)
    datum = Required(dt.date)
    maxBodova = Optional(float)
    stavke = Set("StavkaIspita")
    kolegij = Required(Kolegij)


class StavkaIspita(db.Entity):
    id = PrimaryKey(str)
    brojBodova = Required(float)
    ocjena = Required(int)
    ispit = Required(Ispit)
    student = Required(Student)


db.generate_mapping(check_tables=True, create_tables=True)


# zgodno za testiranje, ne poziva se kad se uključi ovaj file kao modul
if __name__ == "__main__":
    with db_session() as s:
        a = Student(id="1", jmbag="02", ime="Nikola")
        k = Kolegij(id="1", naziv="DWA", semestar=1, studenti=[a])
        i = Ispit(id="1", kolegij=k, datum=dt.datetime.now(), maxBodova=100.)
        si = StavkaIspita(id="1", ispit=i, brojBodova=99.5, ocjena=5, student=a)
