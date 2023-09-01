import sqlalchemy
from sqlalchemy.orm import sessionmaker
from datetime import datetime

from models import create_table, Publisher, Book, Shop, Stock, Sale, upload_data


DSN = 'postgresql://postgres:12345@localhost:5432/library_book_db'
engine = sqlalchemy.create_engine(DSN)
Session = sessionmaker(bind=engine)

def change_publisher(Session, author):
    session = Session()
    sub = session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).join(Publisher).join(Stock).join(Shop).join(Sale)
    if author.isdigit():
        q = sub.filter(Publisher.id_publisher == int(author))
    else:
        q = sub.filter(Publisher.name.like(author))
    for title_book, name_shop, price_sale, date_sale in q.all():
        print(f'Название книги: {title_book} Название магазина: {name_shop} Стоимость: {str(price_sale)} Дата продажи: {date_sale.strftime("%d-%m-%Y")}')
    session.close()

if __name__ == '__main__':
    create_table(engine)
    upload_data(engine)
    author = input('Введите имя автора или его ID для поиска ')
    change_publisher(Session, author)