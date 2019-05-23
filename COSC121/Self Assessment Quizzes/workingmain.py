"""Print all the perfect squares from 2 up to a given maximum."""

def main():
    """Even the main function needs a docstring to keep pylint happy"""
    upper_bound = None
    while upper_bound is None:
        line = input("Enter the upper bound: ")
        if line.isnumeric():
            upper_bound = int(line)
        else:
            print("You must enter a positive number.")
    
    # Make a list of all perfect squares in the given range.
    # We try each number 'num' in turn. To see if 'num'
    # is a perfect square we check each number ('candidate')
    # less than 'num' to see if, when squared, it equals 'num'.
    # If so, 'num' is a perfect square and can be added to the
    # list of perfect squares.
    squares = []
    for num in range(2, upper_bound + 1):
        for candidate in range(1, num):
            if candidate * candidate == num:
                squares.append(num)
    
    print("The perfect squares up to {} are: ".format(upper_bound))
    for square in squares:
        print(square, end=' ')
    print()
    
main()