from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import request

from degree_by_gender_analysis import graph_deg_by_gender

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///survey_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

with app.app_context():
    meta = db.metadata
    meta.reflect(bind=db.engine)
    db.reflect()
    print("heyhey")
    print(meta.tables.values())
    for table in meta.tables.values():
        print("heyhey")
        print(table.name)

class Response(db.Model):
    __tablename__ = 'Response'
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.current_timestamp())
    name = db.Column(db.String(30), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    feedback = db.Column(db.String(500), nullable=False)
    __table_args__ = {'extend_existing': True}  # Add this line


    def __repr__(self):
        return f'<Response {self.name}'

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data.html')
def data():
    return render_template('data.html', plot=graph_deg_by_gender())
    
@app.route('/about.html')
def about():
    return render_template('about.html', the_title='about')

@app.route('/resources.html')
def resources():
    return render_template('resources.html', the_title='resources')


@app.route("/submit", methods=["POST"])
def submit():
    #name = request.form["name"]
    #age = request.form["age"]
    
    year = request.form["year"]
    major = request.form["major"]
    
    confidence = request.form["confidence"]
    imposter = request.form["imposter"]
    support = request.form["support"]
    feedback = request.form["feedback"]
    response = Response(year = year, major = major, confidence = confidence, imposter = imposter, support = support, feedback = feedback)
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