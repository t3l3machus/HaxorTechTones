#!/usr/bin/env python3
# Author: Panagiotis Chartas (t3l3machus)
# Video presentation -> https://youtu.be/RlM6gO_GoHo

from flask import Flask, request, abort
import subprocess

app = Flask(__name__)

# Simple example script showing how improper input handling can cause command injection.
cmd = f'touch "/tmp/*USER_INPUT*" && echo "[+] New file created." >> /dev/null'


# Command injection in GET url parameter
@app.route('/storage', methods=['GET'])
def dashboard():
	if request.method not in ['GET']:
		abort(200, "Bad Request")
	
	user_input = request.args.get('file', '')

	if user_input:
		try:
			subprocess.call(cmd.replace('*USER_INPUT*', user_input), shell=True)
		except Exception:
			pass

	return "Storage loaded successfully. Much wow.", 200



# Command injection in POST request body parameter
@app.route('/create_entry', methods=['POST'])
def create_entry():
	if request.method != 'POST':
		abort(200, "Bad Request")

	entry_id = request.form.get('id', '')
	filename = request.form.get('filename', '')

	if filename:
		try:
			subprocess.call(cmd.replace('*USER_INPUT*', filename), shell=True)
		except Exception:
			pass

	return f"Entry {entry_id} created successfully.", 200



# Command injection in Cookie
@app.route('/session', methods=['POST'])
def session():
	if request.method != 'POST':
		abort(200, "Bad Request")
	
	# Get the 'sessionid' from cookies
	sessionid = request.cookies.get('SESSIONID')

	if sessionid:
		try:
			subprocess.call(cmd.replace('*USER_INPUT*', sessionid), shell=True)
		except Exception:
			pass

	return f"Cookie value {sessionid} processed.", 200



# Command injection in header
@app.route('/head', methods=['GET'])
def head():
	if request.method not in ['GET']:
		abort(200, "Bad Request")
	
	app_key = request.headers.get('AppKey')

	try:
		subprocess.call(cmd.replace('*USER_INPUT*', app_key), shell=True)
	except Exception:
		pass

	return "Header processed.", 200



# Command injection in path
@app.route('/orders/<order_id>', methods=['GET', 'POST'])
def order(order_id):
	if request.method not in ['GET', 'POST']:
		abort(200, "Bad Request")
	
	try:
		subprocess.call(cmd.replace('*USER_INPUT*', order_id), shell=True)
	except Exception:
		pass

	return f"Order {order_id} retrieved successfully.", 200


if __name__ == '__main__':
	app.run(host='127.0.0.1', port=5000, debug=False)
