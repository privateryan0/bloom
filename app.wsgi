import os
# Change working directory so relative paths (and template lookup) work again
os.chdir(os.path.dirname(__file__))

import bottle
# ... build or import your bottle application here ...
# Do NOT use bottle.run() with mod_wsgi
application = bottle.default_app()

import MySQLdb
import sqlite3
from bottle import route, request, template

@route('/')
@route('')
def home():
	return template("home")

@route('/login')
def login():
    return template("login")

@route('/login', method="POST")
def login():
    
	username = request.POST.get('user','').strip()
	password = request.POST.get('pass','').strip()

	db=MySQLdb.connect(host="localhost",user="sauce",passwd="tomato",db="bloom")
	cur = db.cursor() 
	cur.execute("SELECT password FROM user WHERE username='" + username + "';")
	response = cur.fetchall()

	if response:
	    if response[0][0] == password:
		    return "logged in"
	    else:
		    return "incorrect!"
	else:
		return "no match"


@route('/join')
def join():
    return template("join")


@route('/join', method="POST")
def join():
    
    username = request.POST.get('user','').strip()
    password = request.POST.get('pass','').strip()
    
    db=MySQLdb.connect(host="localhost",user="sauce",passwd="tomato",db="bloom")
    
    cur = db.cursor() 
    
    cur.execute("insert into user(username, password) values('" + username + "','" + password + "');")
    response = cur.fetchall()
    db.commit()
    cur.close()
    return response
