from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask Front'

@app.route('/index')
def template_index():
    return render_template('index.html')

@app.route('/user/<name>')
def template_user(name):
    return render_template('user.html', name=name)
