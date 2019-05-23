def thingy(i, j):
    """Does something silly"""
    return (i > 10 and not(j < 5 or i > 20))


def thing(i, j):
    """Does something silly"""
    if i > 10:
        if j < 5 or i > 20:
            return False
        else:
            return True
    else:
        return False

def main():
    """Tells people if they can drive"""

    alcohol_level_string = input("Enter blood alcohol level (mg/100mL): ")
    alcohol_level = float(alcohol_level_string)
    
    age_string = input("Enter age in years: ")
    age = float(age_string)
    
    if (age < 20 and alcohol_level > 0) or alcohol_level >= 50:
        print("You're not allowed to drive")
    elif (age >= 20 and (alcohol_level >= 30 and alcohol_level < 50)):
        print("You're legally allowed to drive, but please don't")
    else:
        print("You're allowed to drive")

main()