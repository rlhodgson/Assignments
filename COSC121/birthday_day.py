current_day = input("Enter the day of your current week ")

current_day = current_day.lower()

day_week = 0

if current_day == "monday":
    day_week =+ 1
elif current_day == "tuesday":
    day_week =+ 2
elif current_day == "wednesday":
    day_week =+ 3
elif current_day == "thursday":
    day_week =+ 4
elif current_day == "friday":
    day_week =+ 5
elif current_day == "saturday":
    day_week =+ 6
elif current_day == "sunday":
    day_week =+ 7
else: 
    print("Sorry please check your spelling")
    

month_of_year = input("Enter month of the year ")
month_of_year = month_of_year.lower()


day_of_month = int(input("Enter the date of {} ".format(month_of_year)))   

jan = 31
feb = 28
march = 31
april = 30
may = 31
june = 30
july = 31
aug = 31
sept = 30
octo = 31
nov = 30
dec = 31

total_days_jan = 31
total_days_feb = 31 + 28
total_days_mar = 31 + total_days_feb
total_days_apr = total_days_mar + 30
total_days_may = total_days_apr + 31
total_days_jun = total_days_may + 30
total_days_jul = total_days_jun + 31
total_days_aug = total_days_jul + 31
total_days_sept = total_days_aug + 30
total_days_oct = total_days_sept + 31
total_days_nov = total_days_oct + 30
total_days_dec = total_days_nov + 31

total_days = 0

if month_of_year == "january":
    month_of_year = int(jan)
    total_days =+ total_days_jan
    in_month = total_days - day_of_month
elif month_of_year == "february":
    month_of_year = int(feb)
    total_days =+ total_days_feb
    in_month = total_days - day_of_month
elif month_of_year == "march":
    month_of_year = int(march)
    total_days =+ total_days_mar
    in_month = total_days - day_of_month
elif month_of_year == "april":
    month_of_year = int(april)
    total_days =+ total_days_apr
    in_month = total_days - day_of_month
elif month_of_year == "may":
    month_of_year = int(may)
    total_days =+ total_days_may
    in_month = total_days - day_of_month
elif month_of_year == "june":
    month_of_year = int(june)
    total_days =+ total_days_jun
    in_month = total_days - day_of_month
elif month_of_year == "july":
    month_of_year = int(july)
    total_days =+ total_days_jul
    in_month = total_days - day_of_month
elif month_of_year == "august":
    month_of_year = int(aug)
    total_days =+ total_days_aug
    in_month = total_days - day_of_month
elif month_of_year == "september":
    month_of_year = int(sept)
    total_days =+ total_days_sept
    in_month = total_days - day_of_month
elif month_of_year == "october":
    month_of_year = int(octo)
    total_days =+ total_days_oct
    in_month = total_days - day_of_month
elif month_of_year == "november":
    month_of_year = int(nov)
    total_days =+ total_days_nov
    in_month = total_days - day_of_month
elif month_of_year == "december":
    month_of_year = int(dec)
    total_days =+ total_days_dec
    in_month = total_days - day_of_month
else:
    print("Sorry please check your spelling")

num_days = total_days - in_month

print(num_days)


"""(day_of_birthday - day_of_year)

birthday_weekday = (day_diff + current_day) % 7

print(birthday_weekday)"""
