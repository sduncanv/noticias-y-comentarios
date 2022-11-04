from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# Conexión a la base de datos Sqlite
class Database:

    def __init__(self):
        self.__engine = create_engine('sqlite:///database.db')
        self.__Session_maker = sessionmaker(bind=self.__engine)
        self.session = self.__Session_maker()