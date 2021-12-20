# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 16:10:05 2021

@author: PC
"""

from flask import Flask, render_template, request
from helper import run_model

#Flask logic
app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])

def index():
    if request.method == "POST":
        #do the logic of retrieving the inputs from the user in the web app
        parameter1=float(request.form["feature 1"])
        parameter2=float(request.form["feature 2"])
        parameter3=float(request.form["feature 3"])
        parameter4=float(request.form["feature 4"])
        
        list_features = [parameter1, parameter2, parameter3, parameter4]
        
        prediction = run_model(list_features)
        
        return render_template("main.html", results=prediction)
    else:
        return render_template("main.html")



if __name__=="__main__":
    app.run(debug=False, port=5435)