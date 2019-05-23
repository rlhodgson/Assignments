"""A program to read a CSV file of rainfalls and print the totals
   for each month.
"""

def read_data(filename):
    """Opens and reads the data within the given filename then closes it"""
    datafile = open(filename)
    data = datafile.readlines()
    datafile.close()  
    return data

def get_month(columns):
    """Returns the month number from the column given"""
    month = int(columns[0])
    return month

def get_num_days(columns):
    """Returns the number of days in the given month within the columns"""
    num_days = int(columns[1])
    return num_days

def get_month_and_days(columns):
    """Returns the month and day as a tuple for further use in the main block"""
    month_and_days = get_month(columns), get_num_days(columns)
    return month_and_days

def get_results(results, columns, month_days):
    """Appends the results of the total rainfall with the month to a list and returns it"""
    month, num_days = month_days
    total_rainfall = 0
    for col in columns[2:2 + num_days]:
        total_rainfall += float(col)
    results.append((month, total_rainfall))    
    return results

def print_outcome(results):
    """Prints the monthly rainfall output"""
    print('Monthly rainfalls')
    for (month, total_rainfall) in results:
        print('Month {:2}: {:.1f}'.format(month, total_rainfall))    

def print_monthly_rainfalls(input_csv_filename):
    """Process the given csv file of rainfall data and print the
       monthly rainfall totals. input_csv_filename is the name of
       the input file, which is assumed to have the month number in
       column 1, the number of days in the month in column 2 and the
       floating point rainfalls (in mm) for each month in the remaining
       columns of the row.
    """
    data = read_data(input_csv_filename)
    results = []  # A list of (month, rainfall) tuples
    for line in data:
        columns = line.split(',')
        month_days = get_month_and_days(columns)
        result = get_results(results, columns, month_days)
    print_outcome(result)

def main():
    """The main function"""
    print_monthly_rainfalls("rainfalls2011.csv")
    
main()