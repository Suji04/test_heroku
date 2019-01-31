from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def say_hello():
	return render_template("index.html")



