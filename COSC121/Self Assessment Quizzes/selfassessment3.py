def silly(i, j):
    """Does something silly"""
    return (j <= i and i > 3 and j < 12)

def re_at_either_end(string):
    """returns a boolean"""
    if string[0:2] == "re" or string[-2:] == "re":
        return True
    else:
        return False
    
def divisible_by_6(number):
    """Returns true if something is divisible by 6"""
    num = number / 6
    nums = int(num)
    if num == nums:
        return True
    else:
        return False
    
def is_trendy(socks_colour, tie_colour):
    """Returns if something is trendy or not"""
    socks = socks_colour.lower()
    tie = tie_colour.lower()
    if socks == "black" and tie == "cream":
        return True
    elif socks == "pinkish" and tie == "cream":
        return True
    else:
        return False
    
def is_viable(angle):
    """Returns true or false"""
    angles = float(angle)
    if angles > 93.011:
        return True
    else:
        return False
    
def level_of_danger(speed, temperature):
    """Returns the level of danger"""
    speeds = float(speed)
    temp = float(temperature)
    danger = 0
    
    if speeds <= 60 and temp > 67:
        danger += 6
        return danger
    elif speeds <=60 and temp <= 67:
        danger += 3
        return danger
    elif speeds > 60 and temp <= 67:
        danger += 4
        return danger
    elif speeds > 60 and temp > 67:
        danger += 10
        return danger
    
print(level_of_danger(59, 65))