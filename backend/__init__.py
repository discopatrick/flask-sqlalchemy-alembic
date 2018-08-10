from flask import Flask

from backend.models import User


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/')
    def hello():
        user_list = ''
        for user in User.query.all():
            user_list += user.fullname + '\n'
        return "Hello World!\n" + user_list

    return app
