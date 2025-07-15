from flask import Flask, render_template
from pymongo import MongoClient
import os

app = Flask(__name__)

MONGO_URI = os.environ.get("MONGO_URI", "mongodb://mongo:27017/")
client = MongoClient(MONGO_URI)
db = client["SERVICE_MANAGER_PROD"]

@app.route("/")
def home():
    collections = db.list_collection_names()
    return render_template("home.html", collections=collections)

@app.route("/ver/<coleccion>")
def ver_coleccion(coleccion):
    docs = list(db[coleccion].find({}, {"_id": 0}))
    return render_template("index.html", data=docs, coleccion=coleccion)
