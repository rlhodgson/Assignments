def combo_string(str1, str2):
    """Returns a string"""
    num_in_first = len(str1)
    num_in_second = len(str2)
    if num_in_first > num_in_second:
        return(str2 + str1 + str2)
    elif num_in_first < num_in_second:
        return(str1 + str2 + str1)
    
def extra_end(s):
    """Returns last 2 letters 3 times"""
    letters = s[-2:]
    return(letters * 3)

def first_half(s):
    """Returns half a string"""
    string = s
    if len(string) % 2 == 0:
        i = len(string) / 2
        j = i + 1
        return string[0:]
    elif len(string) % 2 != 0:
        new_string = string.remove[-1]
        i = len(string) / 2
        j = i + 1
        return string[0:j]
    
print(first_half('WooHoo'))