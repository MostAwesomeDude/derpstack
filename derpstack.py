from datetime import datetime

from flask import Flask
from flask.ext.holster.main import init_holster
from flask.ext.holster.simple import html
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

init_holster(app)
db = SQLAlchemy(app)


class Story(db.Model):
    """
    A cool story.

    Stories should be chilled in order to be quickly servable on the cloud,
    because clouds are made of cold air and suspended water droplets.
    """

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.UnicodeText)
    teller = db.Column(db.Unicode(200))
    date = db.Column(db.DateTime)

    def __init__(self, body, teller):
        self.body = body
        self.teller = teller

        self.date = datetime.now()

    def __repr__(self):
        return "<Story(%s, %s)>" % (self.teller, self.date)


@app.holster("/")
@html("index.html")
def index():
    return {
        "stories": Story.query.all(),
    }

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.debug = True
