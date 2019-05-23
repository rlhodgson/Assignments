def days_in_years(number_of_years):
    """ Return the number of days in the given number of years, assuming
        exactly 365 days in all years.
    """
    days = number_of_years * 365
    return days 
print(days_in_years(3))

def calculate_cartons(eggs):
    """ Calculate the number of cartons needed to hold 
        the specified number of eggs.
    """
    cartons = eggs // 12
    return cartons
print(calculate_cartons(12))
print(calculate_cartons(65))

def dinner_calculator(meal_cost, drinks_cost):
    """ Calculate the cost of dinner during happy hour.
        Takes into consideration:
         - Pre-GST meal and drink costs
         - Happy Hour discounts
         - GST
    """
    drink_discount = drinks_cost * 0.30
    final_drinks_price = drinks_cost - drink_discount
    gst_meal = meal_cost * 1.15
    gst_drinks = final_drinks_price * 1.15
    total_cost = gst_drinks + gst_meal
    return total_cost
print(dinner_calculator(10, 0))
print(dinner_calculator(12, 4))     


def rectangle_area(width, height):
    """ Return the area of a rectangle with the given width and height """
    rect_area = float(width) * float(height)
    return rect_area
print(rectangle_area(5.5, 7.5))

def full_name(first_name, last_name):
    """Return a string consisting of the first name, a space
       and the last name. """
    first_name = str(first_name)
    last_name = str(last_name)
    name = (first_name) + ' ' + (last_name)
    return name

print(full_name('Alex', 6))


def date_string(day_num, month_name, year_num):
    """ Turn the date into a string of the form
            day month, year
    """
    day_num = str(day_num)
    month_name = str(month_name)
    year_num = str(year_num)
    output = (day_num) + ' ' + (month_name) + ', ' + (year_num)
    return output

print(date_string(1, 'December', 1989))

def print_date(year, month, day):
    """ Print out the date, formatted as
            year/month/day
    """
    date = str(year) + "/" + str(month) + "/" + str(day)
    print(date)
    
def get_and_print_rectangle():
    """ Input a rectangle's width and height then print its area """
    rect_width = float(input("Rectangle width? "))
    rect_height = float(input("Rectangle height? "))
    rect_area = rect_width * rect_height
    final_ans = "The area of the rectangle is: {}".format(rect_area)
    print(final_ans)
get_and_print_rectangle()