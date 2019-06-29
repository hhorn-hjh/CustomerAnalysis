from flask import Flask, render_template, request, \
	json, jsonify, url_for, redirect
import sqlite3
import time

import analysis

app = Flask(__name__)


def user_identity(user, password):
	if (user == '') or (password == ''):
		return 2
	rv = sqlite3.connect('customer.db')
	c = rv.cursor()
	c.execute('''
		select password from user where name =?
		''', (user,))
	pwd = ""
	try:
		pwd = c.fetchall()[0][0]
	except IndexError:
		print(pwd)
		rv.close()
		return -1
	else:
		if password == pwd:
			return 1
		else:
			return 0


def user_create(user,password):
	timer = int(time.time())
	rv = sqlite3.connect('customer.db')
	c = rv.cursor()
	ss = '''insert into user values ('%d','%s','%s');''' % \
		 (timer, user, password)
	c.execute(ss)
	rv.commit()
	rv.close()


def login_cookies_check():
	try:
		name = request.cookies.get('name')
		#pwd=request.cookies.get('password')
	except KeyError:
		print("KeyError")
		return False
	else:
		if name == None:
			return False
		else:
			return True


@app.route('/')
def root_index():
	return render_template('login.html')


@app.route('/login', methods=['Get', 'POST'])
def login():
	if request.method == 'GET':
		failed = 'user login'
		return render_template('login.html', failed=failed)
	else:
		username = request.form.get('username')
		password = request.form.get('password')
		if user_identity(username, password) == 1:
			'''
			response = make_response(redirect(url_for('index.html')))
			response.setCookie('name', username)
			return response
			'''
			return redirect(url_for('https://www.baidu.com'))
		else:
			failed = 'invaild username or password'
			return render_template('login.html', failed=failed)


@app.route('/test', methods=['GET', 'POST'])
def hello_world():
	testInfo = {}
	testInfo['name'] = 'xiaoliao'
	testInfo['age'] = '28'
	return json.dumps(testInfo)


@app.route('/testnumber', methods=['GET', 'POST'])
def test_number():
	res = analysis.LRFMC()
	return json.dumps(res)


@app.route('/echarts5')
def echarts5():
	return render_template('echarts5.html')


if __name__ == '__main__':
	app.run()
