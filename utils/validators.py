class Validate:

    def val_create_news(self, data):
        """
        Validate news creation

        This function validates the data to create a news.

        Data to validate:
            - A json with title and content.

        Return a success message if the data is correct otherwise return an error message.
        """
        title = data['title'].replace(' ', '')
        title = title.isdigit()
        content = len(data['content'])

        if (
            title == False and
            len(data['title']) > 10
        ):
            if content > 25:
                return { 'status': 200 }
            else:
                return { 'Error': 'Contenido insuficiente', 'status': 400 }
        else:
            return { 'Error': 'Verifique el título', 'status': 400 }


    def val_read_news(self, data):
        """
        Validate news reading.

        This function validates the data to read a news.

        Data to validate:
            - A json with title.

        Return a success message if the data is correct otherwise return an error message.
        """
        title = data['title'].replace(' ', '')
        title = title.isdigit()

        if (
            title == False and
            len(data['title']) > 0
        ):
            return { 'status': 200 }
        else:
            return { 'Error': 'Verifique el título', 'status': 400 }


    def val_update_news(self, data):
        """
        Validate news update.

        This function validates the data to update a news.

        Data to validate:
            - A json with title_news, title and content.

        Return a success message if the data is correct otherwise return an error message.
        """
        title_news = data['title_news'].replace(' ', '')
        title_news = title_news.isdigit()
        title = data['title'].replace(' ', '')
        title = title.isdigit()
        content = len(data['content'])

        if (
            title == False and 
            title_news == False
        ):
            if content > 25:
                return { 'status': 200 }
            else:
                return { 'Error': 'Contenido insuficiente', 'status': 400 }
        else:
            return { 'Error': 'Verifique el título', 'status': 400 }


    def val_delete_news(self, data):
        """
        Validate deletion of a news.

        This function validates the data to delete a news.

        Data to validate:
            - A json with title.

        Return a success message if the data is correct otherwise return an error message.
        """
        title = data['title'].replace(' ', '')
        title = title.isdigit()

        if (
            title == False and
            len(data['title']) > 0
        ):
            return { 'status': 200 }
        else:
            return { 'Error': 'Verifique el título', 'status': 400 }


    def add_comment(self, data):

        comment = len(data['content_comment'])
        news_id = data['news_id']

        if comment > 0 and news_id > 0:
            return { 'status': 200 }

        else:
            return { 'Error': 'Contenido del comentario vacío', 'status': 400 }