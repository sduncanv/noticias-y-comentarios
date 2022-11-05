# Flask
from flask import Flask, request, render_template

# Validators
from utils.validators import Validate

# Querys
from clases.query import Query


validate = Validate()
query = Query()


app = Flask(__name__)


@app.route('/news/create', methods=['POST'])
def create_news():
    """
    Create a news

    This is the endpoint to create a news and save it in the database.

    Request Body:
        - A json with title and content.

    Return a success message if the data is correct otherwise return an error message.
    """
    try: 
        data = request.json
        val = validate.val_create_news(data)

        if val['status'] == 200:
            res = query.createNews(data)
            return {'message':res}
            
        else:
            return val

    except Exception as e:
        return {'Error': str(e)}


@app.route('/news/read', methods=['GET'])
def read_news():
    """
    Read a news

    This is the endpoint to read a news.

    Request Body:
        - A json with the title.

    Return a success message if the data is correct otherwise return an error message.
    """
    try:
        data = request.json
        val = validate.val_read_news(data)

        if val['status'] == 200:
            res = query.readNews(data)
            return {'message': res}
        else:
            return val

    except Exception as e:
        return {'Error': str(e)}


@app.route('/news/update', methods=['PUT'])
def update_news():
    """
    Update a news

    This is the endpoint to update a news.

    Request Body:
        - A json with the title_news, title and content.
            - title_news: is the json key to search for the news that you want to update.
            - title: is the new title that you want to update.
            - content: is the new content that you want to update.    

    Return a success message if the data is correct otherwise return an error message.
    """
    try:
        data = request.json
        val = validate.val_update_news(data)

        if val['status'] == 200:
            res = query.updateNews(data)
            return { 'message': res }

    except Exception as e:
        return {'Error': str(e)}


@app.route('/news/delete', methods=['DELETE'])
def delete_news():
    """
    Delete a news

    This is the endpoint to update a news.

    Request Body:
        - A json with the title.

    Return a success message if the data is correct otherwise return an error message.
    """
    try:
        data = request.json
        val = validate.val_delete_news(data)

        if val['status'] == 200:
            res = query.deleteNews(data)
            return { 'message': res }

    except Exception as e:
        return {'Error': str(e)}


if __name__ == '__main__':
    app.run(debug = True)