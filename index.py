from flask import Flask, make_response,jsonify
from flask_restful import reqparse, abort, Api, Resource
from data import db_session, new_resources

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
api = Api(app)
def main():
    db_session.global_init("db/blogs.db")
    # для списка объектов
    api.add_resource(new_resources.NewsListResource, '/api/v2/news')
    # для одного объекта
    api.add_resource(new_resources.NewsResource, '/api/v2/news/<int:news_id>')
    app.run()

if __name__ == '__main__':
    main()