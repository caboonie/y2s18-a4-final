# Flask-related imports
from flask import Flask, render_template, url_for, redirect, request, session

# Add functions you need from databases.py to the next line!
from databases import add_student, get_all_students

# Starting the flask app
app = Flask(__name__)

# App routing code here

############################################ HOME ############################################

@app.route('/')
def home():
    return render_template('home.html')

############################################ SIGN-UP ##########################################

@app.route('/signup',methods= ['GET','POST'])
def SignUp ():
    return render_template('signup.html')
    

############################################ LOGIN ############################################

@app.route('/login',methods= ['GET','POST'])
def Login():
    return render_template('login.html')
    

############################################ CATEGORIES #######################################

@app.route('/categories')
def Show():
    return render_template('Categories.html')
    pass

############################################ REQUEST ############################################

@app.route('/request')
def Add():
    return render_template('post_request.html')
    


############################################ PROFILE ############################################

@app.route('/profile')
def Show_prof():
    return render_template('Profile.html')
    pass

##################################################################################################


# Running the Flask app
if __name__ == "__main__":
    app.run(debug=True)
