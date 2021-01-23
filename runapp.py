#!/usr/bin/env python
# -----------------------------------------------------------------------
# runapp.py
# Author: Isabel Zaller
# -----------------------------------------------------------------------

from flask import Flask, make_response
from flask import render_template
import datetime
# from class_declaration import Issue

app = Flask(__name__, template_folder='.')


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def home():
    now = datetime.datetime.now()
    time = now.strftime("%H:%M:%S")

    html = render_template('index.html', time=time)
    response = make_response(html)
    return response


@app.route('/listings', methods=['GET'])
def listings():

    ## fetch data from server

    listings = [1, 2, 3, 4, 5, 6, 7]

    html = render_template('listings.html', listings=listings)
    response = make_response(html)
    return response


@app.route('/details', methods=['GET'])
def details():

    ## fetch data from server

    html = render_template('details.html')
    response = make_response(html)
    return response
