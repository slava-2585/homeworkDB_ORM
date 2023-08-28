import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models import create_table


DSN = 'postgresql://postgres:12345@localhost:5432/library_book_db'
engine = sqlalchemy.create_engine(DSN)

if __name__ == '__main__':
    create_table(engine)

# Session = sessionmaker(bind=engine)
# session = Session()

# session.close()

