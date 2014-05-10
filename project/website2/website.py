# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 16:13:27 2014

@author: sawyer
"""

import random
from pattern.web import *
from pattern.en import *
import numpy
import matplotlib
import math
import matplotlib.pylab as pyl
from urllib2 import Request, urlopen
from urllib import urlencode
import scipy

from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/', methods = ['POST', 'GET'])
def hello_world():
    return render_template('index.html')

    
