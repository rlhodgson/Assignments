def statistics(student_data):
    """Given a list of (name, mark) pairs, returns a tuple
       containing statistics extracted from the list. The tuple elements are
       minimum_mark, maximum_mark, average_mark and top_students. The
       first three are just floating point values. The last one is an
       alphabetically ordered list of the names of all students whose
       marks are equal to the maximum_mark.
    """
    import statistics
    list_of_marks = []
    list_of_names = []
    top_students = []
    for values in student_data:
        mark = values[1]
        mark = float(mark)
        list_of_marks.append(mark)
        name = values[0]
        list_of_names.append(name)
    highest = max(list_of_marks)
    lowest = min(list_of_marks)
    average = (sum(list_of_marks)) / (len(list_of_marks)) 
    
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

data = statistics([('Angus McGurkinshaw', '25\n'), ('Thomas Albert Finkelstein III', '75\n'), ('Myrtle', '50\n')])

print_results(data)