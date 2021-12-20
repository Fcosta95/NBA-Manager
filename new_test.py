from helper1 import choice1
import random
import time
import numpy as np 


def new_game():
    final_script = []
    
    for x in range(10):
        final_script.append('hello' + str(x))
    
    return final_script


#print(new_game())



# =============================================================================
my_team_name = 'Team Blue' #input('name your team: ')
opp_team_name = 'Team Red' #input('name your team: ')
print('your match is against {}'.format(opp_team_name))
pass_text = [' passes it to ', ' puts it in the path of ']
defend_text = [' performs a great block ' , ' stole the ball ', ' huge defensive rebound ']
shoot_text = [ 'hits the ball ' , ' curls it towards the goal ' , ' shoots ']
goal = [' It went IN', 'Perfect Shoot', 'SWOOSH']
no_goal = " he missed it"


#my_team = ['jamie' , 'kurt' , 'andy' , 'jack' , 'sam' , 'michael' , 'roberts' , 'samuel' , 'zack' , 'charlie' , ' bob']
#opp_team = ['jamie' , 'kurt' , 'andy' , 'jack' , 'sam' , 'michael' , 'roberts' , 'samuel' , 'zack' , 'charlie' , ' bob']

import pickle
import pandas as pd
import numpy as np


# =============================================================================
# WKP_OVRL = pd.read_pickle('wkp.p')
# BP_OVRL = pd.read_pickle('bp.p')
# AST_OVRL = pd.read_pickle('ast.p')
# DFP_OVRL = pd.read_pickle('dfp.p')
# AVGP_OVRL = pd.read_pickle('avgp.p')
# =============================================================================

WKP_OVRL = pickle.load(open('wkp.p', 'rb'))
BP_OVRL = pickle.load(open('bp.p', 'rb'))
AST_OVRL = pickle.load(open('ast.p', 'rb'))
DFP_OVRL = pickle.load(open('dfp.p', 'rb'))
AVGP_OVRL = pickle.load(open('avgp.p', 'rb'))

def choice1():
    Weaker_Players = WKP_OVRL[['Player', 'FG%', '3P%', 'FT%', 'ORB', 'DRB', 'SPG', 'BPG', 'APG', 'PPG']].sample(3)
    Best_Players = BP_OVRL[['Player', 'FG%', '3P%', 'FT%', 'ORB', 'DRB', 'SPG', 'BPG', 'APG', 'PPG']].sample(2)
    Assist_Players = AST_OVRL[['Player', 'FG%', '3P%', 'FT%', 'ORB', 'DRB', 'SPG', 'BPG', 'APG', 'PPG']].sample(2)
    Defensive_Players = DFP_OVRL[['Player', 'FG%', '3P%', 'FT%', 'ORB', 'DRB', 'SPG', 'BPG', 'APG', 'PPG']].sample(2)
    Average_Players = AVGP_OVRL[['Player', 'FG%', '3P%', 'FT%', 'ORB', 'DRB', 'SPG', 'BPG', 'APG', 'PPG']].sample(2)
    
    return pd.concat([Weaker_Players,Best_Players,Assist_Players,Defensive_Players, Average_Players])


df = pd.concat([WKP_OVRL,BP_OVRL,AST_OVRL,DFP_OVRL, AVGP_OVRL])
df.to_csv('Overall.csv')

# =============================================================================
# print(df)
# h1 = df[df['Player']== 'James Harden'].sum(axis=1)
# print(h1)
# =============================================================================
team1 = choice1()
team2 = choice1()

my_team = list(team1['Player'])[:6]
opp_team = list(team2['Player'])[:6]


def matchStart(my_team,opp_team) :
    
    my_team_overall = []
    opp_team__overall = []
    for p1 in my_team:
        
        h1 = df[df['Player']== p1].sum(axis=1)
        my_team_overall.append(h1)
        
    for p2 in opp_team:
        
        h2 = df[df['Player']== p2].sum(axis=1)
        opp_team__overall.append(h2)   
    
    print(np.sum(my_team_overall))
    print(np.sum(opp_team__overall))
    
    
    script = []
        
    my_team_score = 0
    opp_team_score = 0
    match_time = 0
    script.append("ref blows the whistle and we're under way!")
    while match_time < 200 :
        goal_or_not = random.randint(0,1)
        whose_ball = random.randint(0,1)
        if whose_ball == 0 :
            #time.sleep(2)
            script.append("the ball is taken and {} {} {} {} ".format(random.choice(opp_team),random.choice(pass_text),random.choice(opp_team),random.choice(shoot_text)))
            #time.sleep(2)
            if goal_or_not == 1 :
                script.append("{} score!".format(opp_team_name))
                opp_team_score += 2
                #time.sleep(2)
                script.append(" it's {} {} ".format(str(my_team_score) , str(opp_team_score)))
                match_time += 1
            else :
                #time.sleep(2)
                script.append("{} {} {} {}".format(random.choice(my_team),random.choice(pass_text),random.choice(my_team),random.choice(shoot_text)))
                #time.sleep(2)
                script.append("{} {}!".format(opp_team_name,no_goal))
                match_time += 1
        else :
            if goal_or_not == 1 :
                    #time.sleep(2)
                    script.append("{} {} {} {}".format(random.choice(my_team),random.choice(pass_text),random.choice(my_team),random.choice(shoot_text)))
                    #time.sleep(2)
                    script.append("{} and {} scored!".format(random.choice(goal), my_team_name) )
                    my_team_score += 2
                    #time.sleep(2)
                    script.append(" it's {} : {} ".format(str(my_team_score) , str(opp_team_score)))
                    match_time += 1
            else :
                    #time.sleep(2)
                    script.append("{} {} {} {}".format(random.choice(my_team),random.choice(pass_text),random.choice(my_team),random.choice(shoot_text)))
                    #time.sleep(2)
                    script.append("{} {}!".format(my_team_name,no_goal))
                    #time.sleep(2)
                    match_time += 1

    if my_team_score > opp_team_score :
        script.append("{} : {} {} win!".format(my_team_score,opp_team_score,my_team_name))
    elif my_team_score < opp_team_score :
        script.append("{} : {} {} win!".format(my_team_score,opp_team_score,opp_team_name))
    else :
        script.append("{} : {} It's a tie".format(my_team_score,opp_team_score))
        
    return script

print(matchStart(my_team, opp_team))