from typing import List, Dict

from views.github_helper import Sanity
import flask
from flask import Flask, request
import mysql.connector

app = Flask(__name__)


def get_token():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'userdb'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT token FROM githubcredentials where uid=1')
    token = cursor.fetchone()[0]
    cursor.close()
    connection.close()

    print(token)
    return token


@app.route('/')
def hello_world():
    reviews = {
                "PR-24": "http://github.com/sirishkumar/project/PR-24",
                "PR-25": "http://github.com/sirishkumar/project/PR-25"
               }
    return flask.render_template('index.html', reviews=reviews)


@app.route('/notifications/<uid>')
def github_notifications(uid: int):
    print(uid)
    #token = get_token()
    sanity = Sanity("5047627c3b3b98bb7da1dded546933c0f2bebd86")
    notifications = sanity.get_notifications("sirishkumar")
    return flask.render_template('notifications.html', notifications=notifications)


@app.route('/shopping')
def index():
    return flask.render_template('shoppint_list.html', key='Vegetables')


@app.route('/shopping', methods=['POST'])
def add_checklist():
    desc = request.form.get('description')
    return flask.render_template('shopping_list.html', key=desc)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
