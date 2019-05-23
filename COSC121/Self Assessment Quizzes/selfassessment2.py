def car_id(model, year):
    """Returns a string of model and year of a car"""
    model_car = str(model)
    year_car = str(year)
    final = ("{0},{1}".format(year_car, model_car))
    return final

def print_time(hour, minute, second):
    """ Print out the time, formatted as
            hour:minute:second
    """
    hours = str(hour)
    mins = str(minute)
    secs = str(second)
    value = ("{0}:{1}:{2}".format(hours, mins, secs))
    print(value)
    
def get_and_print_rect():
    """Returns the area of a rect"""
    width = float(input("Width? "))
    height = float(input("Height? "))
    area = width * height
    print ("Area: {0:.2f}".format(area))
    
def say_little_hi():
    """Asks and prints"""
    name = input("What is your name? ")
    name = name.lower()
    print("Hello there {}.".format(name))
    
