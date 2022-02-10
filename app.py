from flask import Flask, request, render_template
import pickle

application_name = "Tourism"
version = "1.0"

welcome_message = "Hey, Welcome to the journey!".format(application_name, version)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("login.html")
database={'sana@yahoo.com':'123'}

@app.route('/form_login',methods=['POST','GET'])
def login():
    name1=request.form['email']
    pwd=request.form['password']
    if name1 not in database:
	    return render_template('login.html',info='Invalid User')
    else:
        if database[name1]!=pwd:
            return render_template('login.html',info='Invalid Password')
        else:
	         return render_template('index.html',name=name1)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("About.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'password' in request.form and 'email' in request.form:
        # Create variables for easy access
        password = request.form['password']
        email = request.form['email']
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('register.html', msg=msg)

@app.route("/Locate")
def Locate():
    return render_template("Locate.html")

@app.route("/Newsletter")
def Newsletter():
    return render_template("Newsletter.html")

@app.route("/Feedback")
def Feedback():
    return render_template("Feedback.html")

@app.route("/Terms&conditions")
def Termsconditions():
    return render_template("Terms&conditions.html")



if __name__ == "__main__":
    print(welcome_message)
    app.run()



