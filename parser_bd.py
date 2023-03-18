# Импортируйте все нужные библиотеки.
import requests
from bs4 import BeautifulSoup
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import Session, declarative_base

from bs4 import BeautifulSoup


PEP_URL = 'https://peps.python.org/'

Base = declarative_base()

class Pep(Base):
    __tablename__ = 'pep'
    id = Column(Integer, primary_key=True)
    type_status = Column(String(2))
    number = Column(Integer, unique=True)
    title = Column(String(200))
    authors = Column(String(200))

engine = create_engine('sqlite:///sqlite.db', echo=False)
Base.metadata.create_all(engine)

response = requests.get(PEP_URL)
soup = BeautifulSoup(response.text, features='lxml')

section_tag = soup.find('section', {'id': 'numerical-index'})

tbody_tag = section_tag.find('tbody')
print(tbody_tag)
tr_tags = tbody_tag.find_all('tr')

session = Session(bind=engine)

for row in tr_tags:
    cols = row.find_all('td')
    type_status = cols[0].text.strip()
    number = int(cols[1].text.strip())
    title = cols[2].text.strip()
    authors = cols[3].text.strip()
    
    pep = Pep(type_status=type_status, number=number, title=title, authors=authors)
    session.add(pep)
    
session.commit()
