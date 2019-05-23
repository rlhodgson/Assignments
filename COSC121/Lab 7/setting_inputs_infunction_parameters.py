def describe(name='Unknown name', species='unknown', age='unknown'):
    """Prints the information of a animal"""
    print("{0} is a {1}, age: {2}.".format(name, species, age))

def main():
    """Test the describe function """
    describe(name='Angus', species='chipmunk')
    print(30 * '=')
    describe(species='human', name='Marina')
    print(30 * '=')
    describe(age='17')
    print(30 * '=')
    describe('Peter', 'penguin', 10)