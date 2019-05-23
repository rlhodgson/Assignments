def percent_of_goal(donation, goal):
    """Returns the percentage of the goal reached"""
    donation = float(donation)
    goal = float(goal)
    percentage = (donation / goal)*100
    return percentage

def easy_donor_rank(percentage_donated):
    """Returns the level at which a donor is based on
    thier donations"""
    percent = float(percentage_donated)
    if percent <= 0:
        ranking = "Error"
    elif percent >= 1 and percent < 2:
        ranking = "Bronze"
    elif percent >= 2 and percent <= 15:
        ranking = "Silver"
    elif percent > 15:
        ranking = "Gold"
    return ranking
    
        
def donor_rank(percent_donated, amount_donated):
    """Returns the ranking of a donator based on
    percentage and amount"""
    percent = float(percent_donated)
    amount = float(amount_donated)
    if percent <= 0 or amount <= 0:
        ranking = "Error"
    elif (percent >= 1 and percent < 2) and amount < 500:
        ranking = "Bronze"
    elif (percent >=2 and percent <= 15) and amount < 500:
        ranking = "Silver"
    elif percent > 15 and amount < 500:
        ranking = "Gold"
    elif (percent >= 1 and percent < 2) and (amount >= 500 and amount <= 1000):
        ranking = "Silver"
    elif (percent >=2 and percent <= 15) and (amount >= 500 and amount <= 1000):
        ranking = "Silver"
    elif percent > 15 and (amount >= 500 and amount <= 1000):
        ranking = "Gold" 
    elif (percent >= 1 and percent < 2) and amount > 1000:
        ranking = "Gold"
    elif (percent >=2 and percent <= 15) and amount > 1000:
        ranking = "Gold"
    elif percent > 15 and amount > 1000:
        ranking = "Platinum"    
    return ranking

def thank_donor(first_name, last_name, amount, donor_status):
    """Prints a thank you letter to donors"""
    firstname = first_name.capitalize()
    lastname = last_name.upper()
    amount_yes = float(amount)
    amount_final = ("{0:.2f}".format(amount_yes))
    status = donor_status
    final = f'''
----------------------------------------
Note to donor: {lastname}, {firstname}
----------------------------------------
Dear {firstname},
Thank you for your donation of ${amount_final}
to our album campaign.
This makes you a {status} member.
ROCK ON,
Blink 992
========================================'''
    print(final)
    
thank_donor("rachel", "hodgson", 2, "Bronze")