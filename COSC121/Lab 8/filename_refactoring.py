"""Read and process a file of student names and marks.
   Written for COSC121S2.
   Author: Angus McGurkinshaw
   Date: 29 July 2017.
"""

def get_filename():
    """Return the name of the student data file to be processed"""
    return "data.csv"


def read_data(filename):
    """Read and return the contents of the given file.
       The file is assumed to exist, or an exception will occur.
       It is also assumed that each line of the file consists of a
       student name, a comma, and a floating-point mark.
       Returns: a list of (name, mark) tuples, where name is a string
       and mark is a floating-point number.
    """
    lines = open(filename).readlines()
    data = []
    for line in lines: 
        words = line.split(",")
        name = words[0]
        mark = float(words[1])
        tupple_of_name_and_mark = (name, mark)
        data.append(tupple_of_name_and_mark)
    return data
        

def statistics(student_data):
    """Given a list of (name, mark) pairs, returns a tuple
       containing statistics extracted from the list. The tuple elements are
       minimum_mark, maximum_mark, average_mark and top_students. The
       first three are just floating point values. The last one is an
       alphabetically ordered list of the names of all students whose
       marks are equal to the maximum_mark.
    """
    list_of_marks = []
    top_students = []
    for values in student_data:
        mark = values[1]
        mark = float(mark)
        list_of_marks.append(mark)
        
    highest = max(list_of_marks)
    lowest = min(list_of_marks)
    average = (sum(list_of_marks)) / (len(list_of_marks))
    
    #highest = int(highest)
    
    for name, mark in student_data:
        if float(mark) == highest:
            top_students.append(name)
    top_students.sort()
    
    stats = (lowest, highest, average, top_students)  
    return stats
        


def print_results(stats):
    """Print the statistics given. The parameters 'stats' is a
       tuple of the form returned by the 'statistics' function
       above.
    """
    (minimum, maximum, average, top_students) = stats
    print("Minimum mark is: {:.2f}".format(minimum))
    print("Maximum mark is: {:.2f}".format(maximum))
    print("Average mark is: {:.2f}".format(average))
    if len(top_students) == 1:
        print("The top student: {}".format(top_students[0]))
    else:
        print("The top-equal students:\n  {}".format(", ".join(top_students)))


def main():
    """The main function (see module docstring)"""
    filename = get_filename()
    data = read_data(filename)
    stats = statistics(data)
    print_results(stats)

main()