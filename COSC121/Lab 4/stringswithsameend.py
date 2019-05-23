def same_ends(string_1, string_2):
    """Returns true if the two strings have the same first letter and last letter"""
    if ((string_1[0] == string_2[0]) and (string_1[-1] == string_2[-1]) 
    and not(string_1 == string_2)):
        final_answer = True
    else:
        final_answer = False
    return(final_answer)