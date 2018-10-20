from flask import Flask
from flask import jsonify
import json

app = Flask(__name__)
import main


@app.route("/api")
def getEvent():
    return jsonify(main.EventHandler("name", "some date", "this is some description", "site some", "some company",
                             "http://someurl.com").__dict__)
