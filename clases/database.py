from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Models.news import Base, News, Comment

# Conexión a la base de datos Sqlite
class Database:

    def __init__(self):
        self.engine = create_engine('sqlite:///database.db')
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

# db = Database()

# Base.metadata.drop_all(db.engine)
# Base.metadata.create_all(db.engine)