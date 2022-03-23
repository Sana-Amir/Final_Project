from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
import os
import pickle

application_name = "Tourism"
version = "1.0"

welcome_message = "Hey, Welcome to the journey!".format(application_name, version)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///register.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///newsletter.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
db = SQLAlchemy(app)

class Register(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30))
    password = db.Column(db.String(20))

    def __repr__(self):
        return f"Register('{self.email}')"

#app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///newsletter.db'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"Person('{self.email}')"



@app.route('/login')
def hello_world():
    return render_template("login.html")
database={'sana@yahoo.com':'123', 'sanaamir591@yahoo.com':'Laptop123'}

@app.route('/form_login', methods=['POST','GET'])
def login():
    name1=request.form['email']
    pwd=request.form['password']
    if name1 not in database:
        return render_template('login.html',info='Invalid User')
    else:
        if database[name1]!=pwd:
            return render_template('login.html',info='Invalid Password')
        else:
            return render_template('Feedback.html',name=name1)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("About.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    print(request.method)
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = Register(email=email, password=password)
        db.session.add(user)
        db.session.commit()
        flash('You are Registered!')
        return render_template("register.html")

    else:
        return render_template("register.html")



@app.route('/users')
def users():
    users = Register.query.all()
    return render_template('users.html', users=users)

@app.route('/persons')
def persons():
    persons = Person.query.all()
    return render_template('persons.html', persons=persons)


@app.route("/Locate")
def Locate():
    return render_template("Locate.html")

@app.route("/Newsletter", methods=['GET', 'POST'] )
def Newsletter():
    print(request.method)
    if request.method == 'POST':
        email = request.form['email']
        person = Person(email=email)
        db.session.add(person)
        db.session.commit()
        flash('Thank you!')
        return render_template("Newsletter.html")

    else:
        return render_template("Newsletter.html")


@app.route("/Feedback", methods=["GET", "POST"])
def Feedback():
    message = None

    # print(request.method)

    if request.method == "POST":
        email = request.form["email"]
        content = request.form["message"]

        message = f"""
        <strong>Email:</strong> {email} <br/> 
        <strong>Message:</strong> {content}
        """

        return render_template("Feedback.html", message=message)

    return render_template("Feedback.html", message=message)

@app.route("/Terms&conditions")
def Termsconditions():
    return render_template("Terms&conditions.html")

@app.route("/logout")
def logout():
    return render_template("index.html")


if __name__ == "__main__":
    print(welcome_message)
    app.run()

