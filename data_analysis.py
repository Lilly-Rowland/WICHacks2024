from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/data.html')
def data():
    return render_template('data.html', the_title='data')

@app.route('/about.html')
def about():
    return render_template('about.html', the_title='about')

@app.route('/resources.html')
def resources():
    return render_template('resources.html', the_title='resources')
