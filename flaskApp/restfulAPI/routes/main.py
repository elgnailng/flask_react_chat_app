from flask import Blueprint


main = Blueprint('main', __name__)

@main.route('/')
def greet():
    return 'Flask Restful API'

