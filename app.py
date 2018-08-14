# Flask-related imports
from flask import Flask, render_template, url_for, redirect, request
# from flask import session as login_session
# Add functions you need from databases.py to the next line!
from databases import *
# from flask.ext.session import Session
from forgotpass import send_mail
# Starting the flask app
app = Flask(__name__)

# App routing code here
from model import Base,Post
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


# Check Configuration section for more details
# SESSION_TYPE = 'redis'
# app.config['SESSION_TYPE'] = 'filesystem'
# app.secret_key = "VERY SECRET." 
# Session(app)
############################################ HOME ############################################

@app.route('/' ,methods= ['GET','POST'])
def home():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        result = request.form['data']
        return redirect(url_for('display_result', result=result))

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
        return redirect(url_for('home'))
    

############################################ LOGIN ############################################

@app.route('/login.html',methods= ['GET','POST'])
def Login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        user = request.form['username']
        password = request.form['password']
        if check_account(user,password):
            # login_session['username'] = user
            return redirect(url_for('show_prof',username=user))
        else:
            return render_template('login.html')
            

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
        cat = request.form['cat'].strip()
        text = request.form['text'].strip()
        add_post(cat,text)
        return("your post has been published")


############################################ PROFILE ############################################

@app.route('/<string:username>/profile.html')
def show_prof(username):
    # user = query_by_username(login_session['username'])
    user = query_by_username(username)
    return render_template('profile.html',user=user)

############################################ HOME ############################################

@app.route('/forgotpass.html',methods= ['GET','POST'])
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

@app.route('/searchResult/<string:result>',methods= ['GET','POST'])
def display_result(result):
    print(result)
    if request.method == 'GET':
        matches = search(result)
        if matches is None:
            return("No results")
        return render_template('searchResult.html',matches=matches)

# def logout(username):
#     del login_session['username']
##############################################################################################
@app.route('/Jobs')
def jobs_page():
    return render_template('Jobs.html',jobs_posts=query_by_job())

##########################################################################################
@app.route('/sales')
def sales_page():
    return render_template('Sales.html',posts=query_by_job())

##########################################################################################
@app.route('/lostandfound')
def lost_and_found_page():
    return render_template('lost_and_found.html',posts=query_by_job())

##########################################################################################
@app.route('/news')
def news_page():
    return render_template('news.html',posts=query_by_job())

##########################################################################################
@app.route('/others')
def others_page():
    return render_template('others.html',posts=query_by_job())
##########################################################################################
# Running the Flask app
if __name__ == "__main__":
    app.run(debug=True, port=8080)

##############################################################################################


