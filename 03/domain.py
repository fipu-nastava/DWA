from model import Student, Ispit, StavkaIspita, Kolegij
from pony.orm import db_session, select
from uuid import uuid4 as gid, UUID


class Studenti:
    @db_session()
    def listaj():
        # ORM upit
        q = select(s for s in Student)
        # svaku ORM instancu pretvaramo u dictionary
        studenti = [s.to_dict() for s in q]
        return studenti

    @db_session
    def dodaj(s):
        try:
            s["id"] = str(gid())
            # https://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/
            s = Student(**s)
            return True, None
        except Exception as e:
            return False, str(e)

class Kolegiji:
    @db_session()
    def listaj():
        q = select(s for s in Kolegij)
        data = [x.to_dict() for x in q]
        return data

    @db_session
    def dodaj(s):
        try:
            s["id"] = str(gid())
            s = Kolegij(**s)
            return True, None
        except Exception as e:
            return False, str(e)
        
class Ispiti:
    @db_session()
    def listaj():
        q = select(i for i in Ispit)
        # ovaj puta dohvati i listu vezanih entiteta
        data = [x.to_dict(with_collections=True) for x in q]
        for d in data:
            stavke = d["stavke"]
            # Pretvorba u isoformat, npr. 2019-12-04
            d["datum"] = d["datum"].isoformat()
            # Dohvati sve detalje vezanih entiteta
            d["stavke"] = Ispiti.dohvati_stavke(stavke)
        return data 

    @db_session
    def dohvati_stavke(ids):
        q = select(s for s in StavkaIspita if s.id in ids)
        data = [x.to_dict("ocjena student brojBodova") for x in q]
        return data

    @db_session
    def dodaj(s):
        try:
            s["id"] = str(gid())
            stavke = s["stavke"]
            del s["stavke"]  # ne može biti dict/list, mičemo za sada
            s = Ispit(**s)

            # dodaj i stavke sada, i poveži ih na novonastalo zaglavlje
            for stavka in stavke:
                stavka["id"] = str(gid())
                stavka["ispit"] = s
                st = StavkaIspita(**stavka)

            # vraćamo tuple - dvije ili više vrijednosti istovremeno
            return True, None

        except Exception as e:
            return False, str(e)


if __name__ == "__main__":
    studenti = Studenti.listaj()
    print([s.to_dict() for s in studenti])
    ispiti = Ispiti.listaj()
    print([i.to_dict() for i in ispiti])
