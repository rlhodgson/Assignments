"""
Super quiz 1.
This is a module docstring in case you were wondering.
Generates a helpful thank-you note based on user input.
Brought to you by Rachel Hodgson.
"""

def percent_of_goal(donation, goal):
    """ Answer to question one """
    donation = float(donation)
    goal = float(goal)
    percentage = (donation / goal)*100
    percentage = round(percentage, 1)
    return percentage


### Don't need to include easy_donor_rank


def donor_rank(percent_donated, amount_donated):
    """ Answer to question three """
    percent = float(percent_donated)
    amount = float(amount_donated)
    if percent <= 0 or amount <= 0:
        ranking = "Error"
    elif (percent >= 1 and percent < 2) and amount < 500:
        ranking = "Bronze"
    elif (percent >= 2 and percent <= 15) and amount < 500:
        ranking = "Silver"
    elif percent > 15 and amount < 500:
        ranking = "Gold"
    elif (percent >= 1 and percent < 2) and (amount >= 500 and amount <= 1000):
        ranking = "Silver"
    elif (percent >= 2 and percent <= 15) and (amount >= 500 and amount <= 1000):
        ranking = "Silver"
    elif percent > 15 and (amount >= 500 and amount <= 1000):
        ranking = "Gold" 
    elif (percent >= 1 and percent < 2) and amount > 1000:
        ranking = "Gold"
    elif (percent >= 2 and percent <= 15) and amount > 1000:
        ranking = "Gold"
    elif percent > 15 and amount > 1000:
        ranking = "Platinum"    
    return ranking


def thank_donor(first_name, last_name, amount, donor_status):
    """ Answer to question four """
    firstname = first_name.capitalize()
    lastname = last_name.upper()
    amount_yes = float(amount)
    amount_final = ("{0:.2f}".format(amount_yes))
    status = donor_status
    final = f'''----------------------------------------
Note to donor: {lastname}, {firstname}
----------------------------------------
Dear {firstname},
Thank you for your donation of ${amount_final}
to our album campaign.
This makes you a {status} member.
ROCK ON,
Blink 992
========================================'''
    return(final)    
    
    

def main():
    """ Co-ordinates the action. 
    Should get input from user then use your other functions
    to do the rest.
    """
    goal = float(input('Pledge goal? '))
    first_name = input('First name? ')
    last_name = input('Last name? ')
    amount = float(input('Amount donated? '))
    percent = percent_of_goal(amount, goal)
    rank = donor_rank(percent, amount)
    thanks = thank_donor(first_name, last_name, amount, rank)
    print(thanks)
                                     

main()