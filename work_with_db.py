# work_with_db.py
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import Session, declared_attr, declarative_base


# Обычно класс, на основе которого создаётся декларативная база,
# называют так же, как и сам класс декларативной базы.
class Base:

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=Base)


class Pep(Base):
    pep_number = Column(Integer, unique=True)
    name = Column(String(200))
    status = Column(String(20))

    def __repr__(self):
        # При вызове функции print()
        # будут выводиться значения полей pep_number и name.
        return f'PEP {self.pep_number} {self.name}' 



from sqlalchemy import insert, select, update, delete
# work_with_db.py
if __name__ == '__main__':
    engine = create_engine('sqlite:///sqlite.db', echo=False)
    session = Session(engine)

    result = session.execute(
        select(Pep).where(Pep.status == 'Active')
    )
    print(result.all()) 
    
    session.execute(
    update(Pep).where(Pep.pep_number == 8).values(status='Active')
)
    session.commit() 