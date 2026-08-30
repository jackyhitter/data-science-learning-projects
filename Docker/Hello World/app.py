from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Shivam Sharma <strong> #PECkaDarinda </strong>!"

if __name__ == '__main__':
    app.run(debug = True, host = "0.0.0.0")