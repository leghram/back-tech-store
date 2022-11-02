from flask import Flask
from utils.db import db
from flask_sqlalchemy import  SQLAlchemy

from utils.db import db



main_app = Flask(__name__)


main_app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:qwer@localhost/tech_store'
main_app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False


SQLAlchemy(main_app)


@main_app.route('/')
def home():
  return 'hello'

with main_app.app_context():
  db.create_all()


if __name__ == '__main__':
  main_app.run(debug=True)

