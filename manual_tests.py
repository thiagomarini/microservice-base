# -*- coding: utf-8 -*-
from flask import Flask
from config import ROOT

app = Flask(__name__)

@app.route('/tests/hello', methods=['GET'])
def hello():
    return 'hello'