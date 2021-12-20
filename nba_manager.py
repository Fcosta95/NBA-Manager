import random, time
# =============================================================================
# my_team_name = input('name your team: ')
# opp_team_name = input('name your team: ')
# print('your match is against {}'.format(opp_team_name))
# pass_text = [' passes it to ', ' puts it in the path of ']
# defend_text = [' performs a great block ' , ' stole the ball ', ' huge defensive rebound ']
# shoot_text = [ 'hits the ball ' , ' curls it towards the goal ' , ' shoots ']
# goal = [' It went IN!', 'Perfect Shoot!']
# no_goal = " he missed it!"
# =============================================================================

# opp_team = ['jamie' , 'kurt' , 'andy' , 'jack' , 'sam' , 'michael' , 'roberts' , 'samuel' , 'zack' , 'charlie' , ' bob']

def matchStart() :
    
    my_team_score = 0
    opp_team_score = 0
    match_time = 0
    print("ref blows the whistle and we're under way!")
    while match_time < 10 :
        goal_or_not = random.randint(0,1)
        whose_ball = random.randint(0,1)
        if whose_ball == 0 :
            time.sleep(2)
            print("the ball is taken and {} {} {} {} ".format(random.choice(opp_team),random.choice(pass_text),random.choice(opp_team),random.choice(shoot_text)))
            time.sleep(2)
            if goal_or_not == 1 :
                print("{} score!".format(opp_team_name))
                opp_team_score += 2
                time.sleep(2)
                print(" it's {} {} ".format(str(my_team_score) , str(opp_team_score)))
                match_time += 1
            else :
                time.sleep(2)
                print("{} {} {} {}".format(random.choice(my_team),random.choice(pass_text),random.choice(my_team),random.choice(shoot_text)))
                time.sleep(2)
                print("{} {}!".format(opp_team_name,no_goal))
                match_time += 1
        else :
            if goal_or_not == 1 :
                    time.sleep(2)
                    print("{} {} {} {}".format(random.choice(my_team),random.choice(pass_text),random.choice(my_team),random.choice(shoot_text)))
                    time.sleep(2)
                    print("{} {}!".format(my_team_name,goal) )
                    my_team_score += 2
                    time.sleep(2)
                    print(" it's {} {} ".format(str(my_team_score) , str(opp_team_score)))
                    match_time += 1
            else :
                    time.sleep(2)
                    print("{} {} {} {}".format(random.choice(my_team),random.choice(pass_text),random.choice(my_team),random.choice(shoot_text)))
                    time.sleep(2)
                    print("{} {}!".format(my_team_name,no_goal))
                    time.sleep(2)
                    match_time += 1

    if my_team_score > opp_team_score :
        print("{} {} {} win!".format(my_team_score,opp_team_score,my_team_name))
    elif my_team_score < opp_team_score :
        print("{} {} {} win!".format(my_team_score,opp_team_score,opp_team_name))
    else :
        print("{} {} It's a tie".format(my_team_score,opp_team_score))

if __name__ == "__main__":
    matchStart()