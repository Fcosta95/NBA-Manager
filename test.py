# Libraries
from flask import Flask, render_template, request
import random
from helper1 import choice1
import time
#from nba_manager import matchStart
import sys
#from new_test import new_game, matchStart
import pandas as pd
from brincar import matchStart


# Lists
my_team = []
opp_team = []

my_team_name = 'A' #input('name your team: ')
opp_team_name = 'B' #input('name your team: ')
#print('your match is against {}'.format(opp_team_name))
pass_text = [' passes it to ', ' puts it in the path of ']
defend_text = [' performs a great block ' , ' stole the ball ', ' huge defensive rebound ']
shoot_text = [ 'hits the ball ' , ' curls it towards the goal ' , ' shoots ']
goal = [' It went IN!', 'Perfect Shoot!']
no_goal = " he missed it!"


# df = pd.read_csv('Overall.csv')


app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])



# =============================================================================
# def table1():
#     
#     df1 = choice1() 
#     df2 = choice2()
# 
#     return render_template('main.html',tables= [df1.to_html(classes='data'),df2.to_html(classes='data')], titles=['na','FirstTable','SecondTable'])
# 
# 
# 
# =============================================================================
# SAVE LIST

def players():
    df1 = choice1() 
    df2 = choice1()
    
    df = pd.read_csv('Overall.csv')
    
    if request.method == "POST":
        #do the logic of retrieving the inputs from the user in the web app
        PA1=str(request.form["Player A 1"])
        PA2=str(request.form["Player A 2"])
        PA3=str(request.form["Player A 3"])
        PA4=str(request.form["Player A 4"])
        PA5=str(request.form["Player A 5"])
        PB1=str(request.form["Player B 6"])
        PB2=str(request.form["Player B 7"])
        PB3=str(request.form["Player B 8"])
        PB4=str(request.form["Player B 9"])
        PB5=str(request.form["Player B 10"])
        
        
        my_team.append(PA1)
        my_team.append(PA2)
        my_team.append(PA3)
        my_team.append(PA4)
        my_team.append(PA5)
        
        opp_team.append(PB1)
        opp_team.append(PB2)
        opp_team.append(PB3)
        opp_team.append(PB4)
        opp_team.append(PB5)
        
        #opp_team = [PB1, PB2, PB3, PB4, PB5]
        
        #le_list= [my_team, opp_team]
        
        #game_start = run_model(macthStart())
        
        print(my_team, file=sys.stderr)
        print(opp_team, file=sys.stderr)

        #list_all = [PA1, PA2, PA3, PA4, PA5, PB1, PB2, PB3, PB4, PB5]
        
        ret = matchStart(my_team,opp_team)
        
        return render_template('main.html', tables= [df1.to_html(classes='data'),df2.to_html(classes='data')], titles=['na','FirstTable','SecondTable'], results=ret)
    else:
        return render_template("main.html", tables= [df1.to_html(classes='data'),df2.to_html(classes='data')], titles=['na','FirstTable','SecondTable'])





if __name__=="__main__":
    app.run(debug=False, port=3485)

#list_all = [PA1, PA2, PA3, PA4, PA5, PB1, PB2, PB3, PB4, PB5]


# =============================================================================
# def table1():
#    
#     df1 = choice1() 
#     colours = choice2()
#     return render_template('main.html',  tables=[df1.to_html(classes='data')], titles=df1.columns.values, colours=colours)
# 
# def table2():
#     
#     df2 = choice2()
#     return render_template('main.html',  tables=[df2.to_html(classes='data')], titles=df2.columns.values)
# =============================================================================

