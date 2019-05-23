def percent_of_goal(donation, goal):
    """Returns the percentage of the goal reached"""
    donation = float(donation)
    goal = float(goal)
    percentage = (donation / goal)*100
    return percentage 

def donor_rank(percent_donated, amount_donated):
    """ Answer to question three """
    percent = float(percent_donated)
    amount = float(amount_donated)
    if percent <= 0 or amount <= 0:
        ranking = "Error"
    elif (percent > 0 and percent < 2) and amount < 500:
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
    return(ranking)

def ranked_donations(donations, goal):
    """Returns donations and their ranks"""
    final_values = []
    for nums in donations:
        percentage_don = percent_of_goal(nums, goal)
        rank = donor_rank(percentage_don, nums)
        tuplee = (nums, rank)
        final_values.append(tuplee)
    return final_values

donations = [10, 10, 20, 100, 500]
ranks = ranked_donations(donations, 2000)
print(ranks)