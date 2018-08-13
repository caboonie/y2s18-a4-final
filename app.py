# Flask-related imports
from flask import Flask, render_template, url_for, redirect, request, session

# Add functions you need from databases.py to the next line!
from databases import *

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
    if request.method == 'GET':
        return render_template('signup.html')
    else:
        name = request.form['name']
        lastName = request.form['familyName']
        user = request.form['user']
        password = request.form['password']
        mail = request.form['mail']
        loc = request.form['loc']
        add_student(user,password,mail,name,lastName,loc)
        return("HELLO")
    

############################################ LOGIN ############################################

@app.route('/login',methods= ['GET','POST'])
def Login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        user = request.form['username']
        password = request.form['password']
        return(check_account(user,password))
            

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

############################################ HOME ############################################

@app.route('/forgotpass')
def frgt_pwd():
    return render_template('forgotpwd.html')


##############################################################################################

# Running the Flask app
if __name__ == "__main__":
    app.run(debug=True)
