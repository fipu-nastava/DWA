from model import Student, Ispit
from pony.orm import db_session, select


class Studenti:
    @db_session()
    def listaj():
        q = select(s for s in Student)
        studenti = [s.to_dict() for s in q]
        return studenti

class Ispiti:
    @db_session()
    def listaj():
        q = select(i for i in Ispit)
        data = [x.to_dict(with_collections=True, related_objects=True) for x in q]
        return data 


if __name__ == "__main__":
    studenti = Studenti.listaj()
    print([s.to_dict() for s in studenti])
    ispiti = Ispiti.listaj()
    print([i.to_dict() for i in ispiti])
