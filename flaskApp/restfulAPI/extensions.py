from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_migrate import Migrate


api = Api()
db = SQLAlchemy()
migrate = Migrate()