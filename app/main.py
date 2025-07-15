
from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def index():
    data = []
    filepath = os.path.join(os.path.dirname(__file__), "data", "ejemplo.txt")
    with open(filepath, "r") as f:
        for line in f.readlines()[1:]:
            nombre, autorizacion, fecha, grado = line.strip().split(",")
            data.append({
                "nombre": nombre,
                "autorizacion": autorizacion,
                "fecha": fecha,
                "grado": grado
            })
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
