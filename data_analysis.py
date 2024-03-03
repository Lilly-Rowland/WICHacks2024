from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Response(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), nullable = False)
    age = db.Column(db.Integer, nullable = False)
    feedback = db.Column(db.Text, nullable = False)

    def __repr__(self):
        return f'<Response {self.name}'
#app.app_context().push()
#db.create_all()


@app.route('/')
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


@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    age = request.form["age"]
    feedback = request.form["feedback"]

    response = Response(name = name, age = age, feedback = feedback)
    db.session.add(response)
    db.session.commit()

    return "Thank you your response has been recorded"

@app.route("/results")
def results():
    responses = Response.query.all()
    total_responses = len(responses)
    average_age = round(sum([response.age for response in responses])/total_responses, 1)
    unique_names = len(set([response.name for response in responses]))

    return render_template("results.html", responses= responses, total_responses=total_responses, average_age= average_age)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug = True)


