from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
	return "I'm alive"

@app.route('/healthz')
def home():
	return "I'm alive"


def run():
	app.run(host='0.0.0.0',port=80)

def keep_alive():  
	t = Thread(target=run)
	t.start()