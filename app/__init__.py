from flask import Flask



def create_app():
    app = Flask(__name__)
    from app.password_authentication.views import test as test
    app.register_blueprint(test, url_prefix = '/validate')
    return app


