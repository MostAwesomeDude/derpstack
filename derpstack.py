from flask import Flask
from flask.ext.holster.main import init_holster
from flask.ext.holster.simple import html

app = Flask(__name__)

init_holster(app)

@app.holster("/")
@html("index.html")
def index():
    return {"stories": ["Derp!"]}

app.debug = True
