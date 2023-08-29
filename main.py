import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models import create_table, Publisher, Book, Shop, Stock, Sale, upload_data


DSN = 'postgresql://postgres:12345@localhost:5432/library_book_db'
engine = sqlalchemy.create_engine(DSN)
Session = sessionmaker(bind=engine)

def change_publisher(Session):
    author = input('Введите автора для поиска ')

    session = Session()
    q = session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).join(Publisher).join(Stock).join(Shop).join(Sale).filter(Publisher.name.like(author))
    #print ([s[0]] + [s[1]] + [str(s[2])] + [str(s[3])] for s in q.all())
    for s in q.all():
        print(f'{s[0]} | {s[1]} | {str(s[2])} | {str(s[3])}')
    session.close()

if __name__ == '__main__':
    create_table(engine)
    upload_data(engine)
    change_publisher(Session)