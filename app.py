# Flask-related imports
from flask import Flask, render_template, url_for, redirect, request, session

# Add functions you need from databases.py to the next line!
from databases import *

from forgotpass import send_mail
# Starting the flask app
app = Flask(__name__)

# App routing code here

############################################ HOME ############################################

@app.route('/')
def home():
    return render_template('home.html')

############################################ SIGN-UP ##########################################

@app.route('/signup.html',methods= ['GET','POST'])
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

@app.route('/login.html',methods= ['GET','POST'])
def Login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        user = request.form['username']
        password = request.form['password']
        return(check_account(user,password))
            

############################################ CATEGORIES #######################################

@app.route('/categories.html')
def Show():
    return render_template('Categories.html')
    pass

############################################ REQUEST ############################################

@app.route('/request.html',methods= ['GET','POST'])
def Add():
    if request.method == 'GET':
        return render_template('post_request.html')
    else:
        cat = request.form['cat']
        text = request.form['text']
        add_post(cat,text)
        return("your post has been published")


############################################ PROFILE ############################################

@app.route('/profile.html')
def Show_prof():
    return render_template('Profile.html')
    pass

############################################ HOME ############################################

@app.route('/forgotpass',methods= ['GET','POST'])
def frgt_pwd():
    if request.method == 'GET':
        return render_template('forgotpwd.html')
    else:
        email = request.form['email']
        if if_account_exist(email):
            send_mail(email)
            return("Your password has been sent to your email!")
        else:
            return("Sorry, this email does not exists!")

##############################################################################################

# Running the Flask app
if __name__ == "__main__":
    app.run(debug=True, port=8080)
