from flask import Flask, render_template
from app.service import listar

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", tarefas=listar())

app.run(debug=True)
