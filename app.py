from flask import Flask
from flask import request
from flask import render_template
from threading import Thread
from mpmath import mp
app = Flask(__name__)  

@app.route('/')
def my_form():
    return render_template("pi.html")

@app.route('/', methods=['POST'])
def my_form_post():
    text1 = request.form['text1']
    if text1.isnumeric():
      if int(text1) < 250000: 
        mp.dps = int(text1)
        return ('<!DOCTYPE html><html lang="en"><head> <style>*{font-family: courier; color: black;}</style></head><body> <p>'+str(mp.pi)+'</p></body></html>')
      else:
        return("MAX NUMBER: 250,000")
    else:
      return("INVALID")
