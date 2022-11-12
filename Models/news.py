from datetime import datetime
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

Base = declarative_base()

class News(Base):
    __tablename__ = 'news'

    id = Column(Integer(), primary_key=True)
    title = Column(String, nullable=False, unique=True)
    content = Column(String, nullable=False)
    created_at = Column(DateTime(), default=datetime.now())
    comments = relationship('Comment', backref='author', cascade='all, delete')

    def __str__(self):
        return self.title

class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    content_comment = Column(String, nullable=False)
    created_at = Column(DateTime(), default=datetime.now())
    news_id = Column(Integer(), ForeignKey('news.id'))

    def __str__(self):
        return self.title