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

def filter_donations(donor_classification, donations):
    """Returns the list of values in the asked rank"""
    result = []   
    for amount, rank in donations:  
        if rank == donor_classification:
            result.append(amount)  
    return result

def print_donor_report(donations):
    """Returns a report of donatins"""
    total = []
    rank = ['Bronze', 'Silver', 'Gold', 'Platinum']
    name = "Rank"
    sub = "Subtotal"   
    print('{:<15}{:>15}'.format(name, sub)) 
    print('------------------------------')
    for current_rank in rank:
        rank_donations = filter_donations(current_rank, donations)
        sums = sum(rank_donations)
        total.append(sums)
        total_name = "TOTAL"
        print('{:<15}{:>15.2f}'.format(current_rank, sums))
    print('==============================')
    print('{:<15}{:>15.2f}'.format(total_name, sum(total)))   
   
def main():
    """Returns the stuff required"""
    goal = float(input("Campaign goal: "))
    print("Enter the donations received.")
    amount = (input("Amount donated? "))
    amounts = []
    last = []
    error_name = "Errors"
    high_name = "Highest"
    mean_name = "Mean"
    errors = 0
    stats = "STATISTICS"
     
    while amount != "q" and amount != "Q":
        amount = float(amount)
        if amount > 0:
            amounts.append(amount)
        last = ranked_donations(amounts, goal)
        percent = percent_of_goal(amount, goal)
        if donor_rank(percent, amount) == 'Error':
            errors += 1        
        amount = (input("Amount donated? "))   
    maxx = max(amounts)
    mean = sum(amounts)/len(amounts)
    print_donor_report(last)
    print()
    print('{0:^30}'.format(stats))
    print('{:<15}{:>15}'.format(error_name, errors)) 
    print('{:<15}{:>15.2f}'.format(high_name, maxx))    
    print('{:<15}{:>15.2f}'.format(mean_name, mean))
    

main()

