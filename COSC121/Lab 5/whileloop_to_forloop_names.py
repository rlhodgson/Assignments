def print_names2(people):
    """Print a list of people's names, which each person's name
       is itself a list of names (first name, second name etc)
    """
    for person in people:
        to_print = ""
        for name in person:
            to_print += name + " "
        print(to_print)

print_names2([['John', 'Smith'], ['Mary', 'Keyes'], ['Jane', 'Doe']])