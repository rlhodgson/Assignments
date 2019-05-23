def find_programming_engineers(engr101_students, cosc121_students):
    """Finds the programming students that are also doing engineering from
       two sets of data and returns a set of them"""
    engr_cosc = engr101_students.intersection(cosc121_students)
    return engr_cosc

engr = {'Nancy Tennant', 'Simon Wright'}
cosc = {'James Logan', 'Neo'}
print(find_programming_engineers(engr, cosc))