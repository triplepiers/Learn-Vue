from flask import Flask
from sqlalchemy.orm import sessionmaker
from flask_cors import CORS
from src.database import db
from src.user import user

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.config['SECRET_KEY'] = '123456'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

app.register_blueprint(user, url_prefix='/user')


@app.route('/')
def hello_world():  # put application's code here
    db_session = sessionmaker(bind=db)()
    db_session.close()
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)