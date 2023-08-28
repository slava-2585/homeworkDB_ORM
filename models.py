import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Publisher(Base):
    __tablename__ = 'publisher'
    
    id_publisher = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)
    
class Book(Base):
    __tablename__ = 'book'
    
    id_book = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=30))
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey('publisher.id_publisher'))
    
    publisher = relationship(Publisher, backref = 'book')
    
class Shop(Base):
    __tablename__ = 'shop'
    
    id_shop = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)
    
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
    price = sq.Column(sq.Float)
    date_sale = sq.Column(sq.DateTime)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey('stock.id_stock'))
    
    stock = relationship(Stock, backref = 'sale')
    
def create_table(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)