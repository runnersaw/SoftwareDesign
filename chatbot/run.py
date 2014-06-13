''' 
The Chatbot

author: Sawyer
'''

from flask import Flask
from flask import render_template, redirect, request
import ast

conversation = {}

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def pick_nickname_and_password():
	return render_template('pick_nickname.html')

@app.route('/redirect', methods = ['POST', 'GET'])
def get_nickname_and_redirect():
	nickname = str(request.form['nickname'])
	password = str(request.form['password'])
	if check_password(nickname, password):
		url = '/converse/'+nickname
		return redirect(url)
	return redirect('/')

@app.route('/converse/<nickname>', methods = ['POST', 'GET'])
def index(nickname):
	responses = []
	if nickname in conversation:
		responses = conversation[nickname]
	return render_template('main.html', nickname=nickname, responses=responses)

@app.route('/respond/<nickname>', methods = ['POST', 'GET'])
def respond(nickname):
	search = str(request.form['searchkey'])
	text = take_input(search, nickname)
	url = '/converse/'+nickname
	return redirect(url)

@app.route('/logout/<nickname>', methods = ['POST', 'GET'])
def logout(nickname):
	clear_conversation(nickname)
	return redirect('/')

@app.route('/make_responses', methods = ['POST', 'GET'])
def suggest_responses():
	unanswered = make_list()
	return render_template('help.html', unanswered=unanswered)

@app.route('/help_redirect/<post>', methods = ['POST', 'GET'])
def add_response(post):
	value = request.form[post]
	add_entry(post, value)
	remove_from_unresponded(post)
	return redirect('/make_responses')

def check_password(user, password):
	f = open('users.txt', 'r+')
	x = f.read()
	y = ast.literal_eval(x)
	if user not in y:
		add_user(user, password)
		return True
	if y[user] == password:
		return True
	return False

def add_user(user, password):
	f = open('users.txt', 'r+')
	x = f.read()
	y = ast.literal_eval(x)
	y[user] = password
	z = str(y)
	new_file = open('users.txt', 'w')
	new_file.write(z)
	new_file.close()

def add_entry(key, value):
	f = open('responses.txt', 'r+')
	x = f.read()
	y = ast.literal_eval(x)
	y[key] = value
	z = str(y)
	new_file = open('responses.txt', 'w')
	new_file.write(z)
	new_file.close()

def make_dictionary():
	f = open('responses.txt', 'r+')
	x = f.read()
	return ast.literal_eval(x)

def make_list():
	f = open('unresponded.txt', 'r+')
	x = f.read()
	return ast.literal_eval(x)

def find_response(key):
	dictionary = make_dictionary()
	if key in dictionary:
		return dictionary[key]
	add_to_unresponded(key)
	return None

def add_to_unresponded(key):
	f = open('unresponded.txt', 'r+')
	x = f.read()
	l = ast.literal_eval(x)
	if key not in l:
		l.append(key)
	l = str(l)
	new_file = open('unresponded.txt', 'w')
	new_file.write(l)
	new_file.close()

def remove_from_unresponded(key):
	f = open('unresponded.txt', 'r+')
	x = f.read()
	l = ast.literal_eval(x)
	l.remove(key)
	l = str(l)
	new_file = open('unresponded.txt', 'w')
	new_file.write(l)
	new_file.close()

def take_input(key, user):
	if user in conversation:
		conversation[user].append(key)
	else:
		conversation[user] = []
		conversation[user].append(key)
	res = find_response(key)
	if res == None:
		res = "Sorry, we don't have a response for that yet"
	conversation[user].append(res)
	return res

def clear_conversation(user):
	conversation[user] = []

if __name__ == '__main__':
	app.run()