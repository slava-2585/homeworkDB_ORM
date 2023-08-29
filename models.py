import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import json

Base = declarative_base()

class Publisher(Base):
    __tablename__ = 'publisher'
    
    id_publisher = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)
    
    def __str__(self):
        return f'{self.name}'
    
    
class Book(Base):
    __tablename__ = 'book'
    
    id_book = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=50))
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey('publisher.id_publisher'))
    
    publisher = relationship(Publisher, backref = 'book')
    
    def __str__(self):
        return f'{self.title}'
    
    
class Shop(Base):
    __tablename__ = 'shop'
    
    id_shop = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)
    
    def __str__(self):
        return f'{self.name}'
    
        
class Stock(Base):
    __tablename__ = 'stock'
    
    id_stock = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey('book.id_book'))
    id_shop = sq.Column(sq.Integer, sq.ForeignKey('shop.id_shop'))
    count = sq.Column(sq.Integer)
    
    book = relationship(Book, backref = 'stock')
    shop = relationship(Shop, backref = 'stock')

    
class Sale(Base):
    __tablename__ = 'sale'
    
    id_sale = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.String(length=10))
    date_sale = sq.Column(sq.DateTime)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey('stock.id_stock'))
    count = sq.Column(sq.Integer)
    
    stock = relationship(Stock, backref = 'sale')
    
    def __str__(self):
        return f'{self.price}, {self.date_sale}'
    
    
def create_table(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    
def upload_data(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    with open('tests_data.json') as json_file:
        data = json.load(json_file)
        for s in data:
            if s['model'] == 'publisher':
                d = Publisher(id_publisher = s['pk'], name = s['fields']['name'])
                session.add(d)
                session.commit()
            elif s['model'] == 'book':
                d = Book(id_book = s['pk'], title = s['fields']['title'], id_publisher = s['fields']['id_publisher'])
                session.add(d)
                session.commit()
            elif s['model'] == 'shop':
                d = Shop(id_shop = s['pk'], name = s['fields']['name'])
                session.add(d)
                session.commit()
            elif s['model'] == 'stock':
                d = Stock(id_stock = s['pk'], id_book = s['fields']['id_book'], id_shop = s['fields']['id_shop'], count = int(s['fields']['count']))
                session.add(d)
                session.commit()
            elif s['model'] == 'sale':
                d = Sale(id_sale = s['pk'], price = s['fields']['price'], date_sale = s['fields']['date_sale'], count = int(s['fields']['count']), id_stock = int(s['fields']['id_stock']))
                session.add(d)
                session.commit()
    session.close()