import os

import flask
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)


application = flask.Flask(__name__)

# Only enable Flask debugging if an env var is set to true
application.debug = os.environ.get('FLASK_DEBUG') in ['true', 'True']

# Get application version from env
app_version = os.environ.get('APP_VERSION')

# make sure the database username, database password and
# database name are correct
application.config['USERPASS'] = 'mysql+pymysql://' + \
                                 os.environ.get('DB_USERNAME') + \
                                 ":" + \
                                 os.environ.get('DB_PASSWORD') + \
                                 '@'
# there is no socket
application.config['SQLALCHEMY_DATABASE_URI'] = application.config['USERPASS'] + \
                                                os.environ.get('DB_SERVER') + \
                                                os.environ.get('DB_NAME')

application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(application)
# Get cool new feature flag from env
enable_cool_new_feature = os.environ.get('ENABLE_COOL_NEW_FEATURE') in ['true', 'True']


@application.route('/')
def hello_world():
    message = "Hello, world!"
    return flask.render_template('index.html',
                                 title=message,
                                 flask_debug=application.debug,
                                 app_version=app_version,
                                 enable_cool_new_feature=enable_cool_new_feature)


@application.route('/users')
def get_add_users():
    users = User.query.all()
    users_list = [{'id': user.id, 'username': user.username, 'email': user.email} for user in users]
    return jsonify(users_list)


if __name__ == '__main__':
    application.debug = True
    application.run(host='0.0.0.0')
