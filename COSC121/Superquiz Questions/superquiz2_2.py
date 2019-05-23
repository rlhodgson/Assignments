def filter_donations(donor_classification, donations):
    """Returns the list of values in the asked rank"""
    result = []
    
    for amount, rank in donations:  
        if rank == donor_classification:
            result.append(amount)
    
    return result
            

donations = [(100.0, "Gold"), (10.0, "Bronze"), (-100.0, "Error"), (10.0, "Gold")]
super_gold_donors = filter_donations("Gold", donations)
print(super_gold_donors)