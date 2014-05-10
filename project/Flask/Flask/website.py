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

def sentiment_to_text(company):
    #set up Twitter search engine
    t = Twitter(language='en')
    
    #initalize variables
    string = []
    output = []
    k=0
    
    #Check that there is a result, and use that as reference tweet id later
    for tweet in t.search(company, start=None, count=1):
        i = tweet.id
        current_date = unicode_tweet_date_reformat(tweet.date)
        
    #loop that runs until you can't pull more data from Twitter
    running = True
    while running:
        try:
            string.append('') #initalize variable string that stores all the tweets
            totSentimentTemp = 0 #initialize temporary sentiment variable
            count = 1.0
            i = unicode(int(i)-50000000000000*(k)) #look further back in twitter's archive
            if t.search(company, start=i, count=1)==[]:
                raise SystemExit("Sorry, your company doesn't have any recent tweets") #break the try except statement
            for tweet in t.search(company, start=i, count=100):
                date = tweet.date
                dateNumerical = unicode_tweet_date_reformat(tweet.date)
                hoursAgo = reformatted_date_subtraction(current_date, dateNumerical)
                x = sentiment(tweet.text)
                totSentimentTemp = (totSentimentTemp*(count-1)+x[0])/count
                count+=1
                string[k] += tweet.text
            k+=1 
            output.append([date, hoursAgo, totSentimentTemp])
        except:
            running = False
    return output
        
def unicode_tweet_date_reformat(unicodeDate):
    month = unicodeDate[4:7]
    date = unicodeDate[8:10]
    hour = unicodeDate[11:13]
    date = str(date)
    if month == 'Jan':
        month = 1
    if month == 'Feb':
        month = 2
    if month == 'Mar':
        month = 3
    if month == 'Apr':
        month = 4
    if month == 'May':
        month = 5
    if month == 'Jun':
        month = 6
    if month == 'Jul':
        month = 7
    if month == 'Aug':
        month = 8
    if month == 'Sep':
        month = 9
    if month == 'Oct':
        month = 10
    if month == 'Nov':
        month = 11
    if month == 'Dec':
        month = 12
    date = int(date)
    hour = int(hour)
    return (month, date, hour)  
    
def reformatted_date_subtraction(current_date, prev_date):
    hoursAgo = current_date[2] - prev_date[2]
    rollover = 0
    if hoursAgo < 0:
        hoursAgo += 24
        rollover = 1
    daysAgo = current_date[1]-prev_date[1]-rollover
    if daysAgo < 0:
        if prev_date[0] == 1 or prev_date[0] == 3 or prev_date[0] == 5 or prev_date[0] == 7 or prev_date[0] == 8 or prev_date[0] == 10 or prev_date[0] == 12:
            daysAgo+=31
        elif prev_date[0] == 2:
            daysAgo+=28
        else:
            daysAgo+=30
    hoursAgo+=24*daysAgo
    return hoursAgo

from flask import Flask, render_template, request, redirect
app = Flask(__name__)

email_addresses = []

@app.route('/', methods = ['POST', 'GET'])
def hello_world():
    return render_template('index.html')

@app.route('/signup', methods = ['POST', 'GET'])
def signup():
    search = request.form['searchkey']
    timestep = request.form['timestep']
    print("The search is for '" + search + "'")
    print("The timestep is '" + timestep + "'")
    return redirect('/')
    
@app.route('/search', methods = ['POST', 'GET'])
def search():
    search = request.form['searchkey']
    timestep = request.form['timestep']
    print("The search is for'" + search + "'")
    print("The timestep is '" + timestep + "'")
    results = sentiment_to_text(search)
    dates = []
    hours = []
    sentiments = []
    for entry in results:
        temp = entry[0]
        entry[0] = temp[0:16]
        dates.append(entry[0])
        hours.append(entry[1])
        sentiments.append(entry[2])
    pyl.plot(hours, sentiments, 'bo-')
    pyl.savefig('static/sentiment.png')
    return render_template('sentiment.html', dates=dates, hours=hours, sentiments=sentiments)
    
if __name__ == "__main__":
    app.run()
    