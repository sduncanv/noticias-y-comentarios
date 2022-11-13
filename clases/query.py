from clases.database import Database
from Models.news import News as modelNews
from Models.news import Comment as modelComment
from flask import jsonify
db = Database()


class Query:

    def createNews(self, data):
    
        news_exists = db.session.query(modelNews).filter(
            modelNews.title == data['title']
        ).first()

        if news_exists == None:
            db.session.bulk_insert_mappings(modelNews, [data])
            db.session.commit()
            db.session.close()
            
            return 'Noticia creada'

        else:
            return 'Noticia existente'
    

    def readNews(self, data):

        news_to_read = db.session.query(modelNews).filter(
            modelNews.title == data['title']
        ).first()

        if news_to_read != None:
            #list = [com.content_comment for com in news_to_read.comments]
            #print(f' ++++ {list}')
            return {
                'title': news_to_read.title,
                'content': news_to_read.content,
                'comments': [com.content_comment for com in news_to_read.comments]
            }

        else:
            return 'La noticia no existe'
    

    def updateNews(self, data):

        db = Database()
        news_to_update = db.session.query(modelNews).filter(
            modelNews.title == data['title_news']
        ).first()

        if news_to_update != None:

            news_to_update.title = data['title']
            news_to_update.content = data['content']

            db.session.add(news_to_update)
            db.session.commit()
            db.session.close()

            return 'Noticia actualizada'

        else:
            return 'La oticia no existente'


    def deleteNews(self, data):

        news_to_delete = db.session.query(modelNews).filter(
            modelNews.title == data['title']
        ).first()

        if news_to_delete != None:
            # db.session.query(modelNews).filter(
            #     modelNews.title == data['title']
            # ).delete()
            db.session.delete(news_to_delete)
            db.session.commit()
            db.session.close()

            return 'Noticia eliminada'

        else:
            return 'La oticia no existente'

    
    def createComment(self, data):
        
        news_exists = db.session.query(modelNews).filter(
            modelNews.id == data['news_id']
        ).first()
        
        if news_exists != None:
            comment = modelComment(
                content_comment = data['content_comment'],
                author = news_exists
            )
            db.session.add(comment)
            db.session.commit()
            db.session.close()

            return 'Comentario agregado'
        
        else:
            return 'No existe la noticia'
