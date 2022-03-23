from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    a = 1
    b = 2
    c = a + b
    return f"Hello Flask added_value{c}"
