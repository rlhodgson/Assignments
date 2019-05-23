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
         
    
print_donor_report([])