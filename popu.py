from Models.news import News, Comment
from clases.database import Database

db = Database()

# new_news = News(
#     title='Noticia 1',
#     content='Contenido 1'
# )
# db.session.add(new_news)
# db.session.commit()

# news=[
#     {
#         'content_comment': 'Comment 1.1'
#     },
#     {
#         'content_comment': 'Comment 1.2'
#     },
#     {
#         'content_comment': 'Comment 1.3'
#     },
#     {
#         'content_comment': 'Comment 1.4'
#     },
# ]

# n_ews = db.session.query(News).filter(News.id==1).first()

# for new in news:
#     new_comment = Comment(
#         content_comment=new['content_comment'],
#         author=n_ews
#     )
#     db.session.add(new_comment)
#     db.session.commit()

news_to_delete = db.session.query(News).filter(News.id==1).first()

db.session.delete(news_to_delete)
db.session.commit()