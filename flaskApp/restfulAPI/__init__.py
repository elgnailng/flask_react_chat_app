from flask import Flask 

from .extensions import db, migrate
from .routes.main import main
from .models.messages import MessageModel
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask import request
from time import time

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databse.db'  #'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    restfulAPI = Api(app)
    migrate.init_app(app, db)

    app.register_blueprint(main)

    resouces_fields = {
        'uid' : fields.String,
        'text': fields.String,
        'createdAt': fields.String,
        'photoURL': fields.String,
    }

    class ChatRepository(Resource):
        @marshal_with(resouces_fields)
        def get(self):
            result = MessageModel.query.all()
            return result


        @marshal_with(resouces_fields)
        def put(self):
            # message_put_args = reqparse.RequestParser()
            # message_put_args.add_argument("text", type=str, help="message from the user")
            # message_put_args.add_argument("createdAt", type=int, help="timestamp from the user")
            # message_put_args.add_argument("uid", type=int, help="unique id of the user")
            # message_put_args.add_argument("photoURL", type=str, help="url of the user's profile picture")
            # args = message_put_args.parse_args(http_error_code=300)
            args = request.json.get
            message = MessageModel(uid=args("uid"), text=args("text"), createdAt=args('createdAt'), photoURL=args("photoURL"))
            db.session.add(message)
            db.session.commit()
            return message, 201

    restfulAPI.add_resource(ChatRepository, "/messages")

    return app