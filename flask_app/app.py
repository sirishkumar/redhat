import json
import os
import sys

from data import db_session
from data.githubapitoken import GithubAPIToken
from views.github_helper import Sanity
import flask
from flask import Flask, request
import sqlalchemy.orm

folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return flask.render_template('index.html')


@app.route('/user', methods=['POST'])
def user():
    data = request.data
    data_string = data.decode('utf-8')
    data_dict = json.loads(data_string)

    apitoken = GithubAPIToken()
    apitoken.id = data_dict['user']
    apitoken.email = data_dict['email']
    apitoken.hashed_token = data_dict['token']

    session: sqlalchemy.orm.Session = db_session.create_session()
    session.add(apitoken)
    session.commit()

    return "User created successfully", 200


@app.route('/notifications/<username>')
def github_notifications(username: int):
    session = db_session.create_session()
    githubapi: GithubAPIToken = session.query(GithubAPIToken).filter_by(id=username).one()
    sanity = Sanity(githubapi.hashed_token)
    notifications = sanity.get_notifications("sirishkumar")
    return flask.render_template('notifications.html', notifications=notifications)


def main():
    configure()
    app.run(host='0.0.0.0')


def configure():
    setup_db()


def setup_db():
    db_session.global_init_mysql()


if __name__ == '__main__':
    main()
else:
    configure()
