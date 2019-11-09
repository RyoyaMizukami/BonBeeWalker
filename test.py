#using: utf-8
from flask import Flask, render_template, session, redirect, url_for, escape, request
import os

app = Flask(__name__)

API_key = os.environ.get('gmap_API')

@app.route('/')
def index():
    return render_template('commons/api_test.html', API_key = API_key)

if __name__ == "__main__":
    app.run()
