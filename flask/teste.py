from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

test = Flask(__name__)
test.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

bd = SQLAlchemy(test)
migrate = Migrate(test, bd)

class User(bd.Model):
    id = bd.Column(bd.Integer, primary_key=True)
    name = bd.Column(bd.String(128))

if __name__ == '__main__':
    test.run(debug=True)