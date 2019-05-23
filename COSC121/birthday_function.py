def get_birthday_weekday():
    """calculating the day of the week a birthday will be on"""
    current_day = int(input("Enter the number corresponding to the day of the week "))
    day_of_year = int(input("Enter day of the year "))
    day_of_birthday = int(input("Enter the day of the year your birthday is "))    
    day_diff = (day_of_birthday - day_of_year)
    birthday_weekday = (day_diff + current_day) % 7
    print(birthday_weekday)

get_birthday_weekday()