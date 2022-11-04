from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

class News(Base):

    __tablename__ = 'news'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, unique=True)
    content = Column(String, nullable=False)


class Comment(Base):

    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    content_comment = Column(String, nullable=False)
    title_new = Column(String, ForeignKey('news.title'))
    news = relationship(News, backref=backref('comments'))
    