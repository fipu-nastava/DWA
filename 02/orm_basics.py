from pony.orm import *
from uuid import uuid4 as gid, UUID
import os

# otkomentirati ako se želi vidjeti pozadinske upite prema bazi
# set_sql_debug(True, show_values=True)

#########
# MODEL #
#########

# spajanje na bazu
db = Database()

# os.remove("02/database.sqlite")
# db.bind(provider='sqlite', filename='database.sqlite', create_db=True)
db.bind(provider='postgres', user='postgres', password='dwa', host='localhost', database='dwa')

# klasa modela
class Student(db.Entity):
    id = PrimaryKey(str)
    jmbag = Required(str)
    ime = Required(str)
    prezime = Required(str)
    spol = Required(str, max_len=1)
    polozeno_ispita = Optional(int, default=0)


# automatsko generiranje tablica u bazi
db.generate_mapping(check_tables=True, create_tables=True)


### Insert korištenjem SQL-a
@db_session()
def ovako_radi_sql_insert(s):
    if id not in s:
        s["id"] = str(gid())

    s = s.copy()  # ne diraj mi ulaznu referencu
    db.execute("""insert into Student (id, jmbag, ime, prezime, spol)
               values ($id, $jmbag, $ime, $prezime, $spol)""", s)

### Insert korištenjem ORM-a
@db_session()
def ovako_radi_orm_insert(s):
    if id not in s:
        s["id"] = str(gid())

    instanca = Student(**s)  # pogledaj http://bit.ly/2FvjCab


### Dohvati listu id-eva studenata, ručno pomoću SQL-a
@db_session()
def dohvati_listu_ideva_rucno_sqlom():
    ids = []
    results = db.select("select id, ime from Student")  # namjerno stavljeno i 'ime' iako je višak
    for s in results:
        ids += [s.id]

    return ids


### Dohvati listu id-eva studenata ORM-om
@db_session
def dohvati_listu_ideva_ormom():
    ids = select(s.id for s in Student)
    return ids


### Dohvati studenta po id-u, ručno pomoću SQL-a 
@db_session()
def select_with_sql(id_lista_za_dohvat):
    records = []
    for id in ids:  # N-upita, jedan po jedan
        record = db.select("select * from Student where id = $id")
        records.append(record)

    return records


### Dohvati studenta po id-u, automatski pomoću ORM-a
@db_session()
def select_with_orm(id_lista_za_dohvat):
    for id in ids:  # N-upita, jedan po jedan
        s = Student[id]

    ## alternativno, jedan upit za sve
    query = select(s for s in Student if s.id in id_lista_za_dohvat)
    return query[:]


### Update ručno SQL-om
@db_session()
def update_ispiti_sql(id_ovi):
    for id in id_ovi:
        db.execute("update Student set polozeno_ispita = polozeno_ispita + 1 where id = $id")


### Update ručno SQL-om
@db_session()
def update_ispiti_orm(studenti):
    for s in studenti:
        trenutno_polozeno = s.polozeno_ispita or 0
        s.polozeno_ispita = trenutno_polozeno + 1
    

### Kreiranje dict-ova, zamisli da su došli kao JSON iz front-enda
s0 = {"ime": "Jelena", "prezime": "Jurić", "jmbag": "00362345123", "spol": "Ž"}
s1 = {"ime": "Hrvoje", "prezime": "Horvat", "jmbag": "00360001", "spol":"M"}
s2 = {"ime": "Ivana", "prezime": "Ivić", "jmbag": "00360001", "spol": "Ž"}
s3 = {"ime": "Marko", "prezime": "Marković", "jmbag": "00365111342", "spol": "M"}

ovako_radi_sql_insert(s0)
ovako_radi_sql_insert(s1)
ovako_radi_orm_insert(s2)
ovako_radi_orm_insert(s3)

with db_session() as s:
    ids = dohvati_listu_ideva_rucno_sqlom()
    ids_2 = dohvati_listu_ideva_ormom()

    assert set(ids) == set(ids_2), "Greška: trebalo bi biti isto!"

    print("Postoje sljedeći id-ovi studenata:", ids)

    # dohvati po ID-u 
    studenti1 = select_with_sql(ids)
    update_ispiti_sql(ids)

    studenti2 = select_with_orm(ids)
    update_ispiti_orm(studenti2)
