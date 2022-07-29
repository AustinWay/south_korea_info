#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

DEVELOPMENT_ENV = True

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class SeoulDistricts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    english_name = db.Column(db.String(150), unique=True, nullable=False)
    korean_name = db.Column(db.String(150), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
    image_file = db.Column(db.String(50), nullable=False, default='default.jpg')

    def __repr__(self):
        return f"('{self.english_name}', '{self.korean_name}','{self.description}','{self.image_file}')"

app_data = {
    "name":         "Seoul Guide",
    "description":  "A basic Flask app using bootstrap to describe Seoul",
    "author":       "Austin Way",
    "project_name": "Seoul Guide",
    "keywords":     "flask, webapp, Seoul, Districts, Provinces, Guide"
}

@app.route('/')
def index():
    return render_template('index.html', app_data=app_data)


@app.route('/districts_of_Seoul')
def districts_of_Seoul():
    return render_template('districts_of_Seoul.html', app_data=app_data)


@app.route('/administrative_divisions_of_South_Korea')
def administrative_divisions_of_South_Korea():
    return render_template('administrative_divisions_of_South_Korea.html', app_data=app_data)


@app.route('/provinces_of_South_Korea')
def provinces_of_South_Korea():
    return render_template('provinces_of_South_Korea.html', app_data=app_data)

@app.route('/numbers')
def numbers():
    return render_template('numbers.html', app_data=app_data)

if __name__ == '__main__':
    app.run(debug=DEVELOPMENT_ENV)
