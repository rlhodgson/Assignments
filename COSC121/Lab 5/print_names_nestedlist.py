def print_names(names):
    """Prints names"""
    i = 0
    while i < len(names):
        name = names[i]
        print(name)
        i += 1
        
def print_names2(people):
    """Print a list of people's names, which each person's name
       is itself a list of names (first name, second name etc)
    """
    i = 0
    while i < len(people):
        to_print = ""
        j = 0
        while j < len(people[i]):
            to_print += (people[i])[j] + " "
            j += 1
        print(to_print)
        i += 1
        
print_names2([['John', 'Smith'], ['Mary', 'Keyes'], ['Jane', 'Doe']])
