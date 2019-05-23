"""Print all the perfect squares from zero up to a given maximum.
   This version is refactored to make it more understandable
   and more maintainable."""

def read_bound():
    """Reads the upper bound from the standard input (keyboard).
       If the user enters something that is not a positive integer
       the function issues an error message and retries
       repeatedly"""
    
    upper_bound = None
    while upper_bound is None:
        line = input("Enter the upper bound: ")
        if line.isnumeric():
            upper_bound = int(line)
        else:
            print("You must enter a positive number.")
    return upper_bound


def is_perfect_square(num):
    """Return true if and only if num is a perfect square"""
    for candidate in range(1, num):
        if candidate * candidate == num:
            return True


def squares_up_to_n(upper_bound):
    """ Returns the list of all perfect squares between 2 and n """
    
    squares = []
    for num in range(2, upper_bound + 1):
            if is_perfect_square(num) == True:
                squares.append(num)
    return squares



def print_squares(upper_bound, squares):
    """Print a given list of all the squares up to a given upper bound"""
    
    
    print("The perfect squares up to {} are: ".format(upper_bound))
    for square in squares:
        print(square, end=' ')
    print()


def main():
    """Every home should have one"""
    upper_bound = read_bound()
    squares = squares_up_to_n(upper_bound)
    print_squares(upper_bound, squares)
    # AND WHAT GOES HERE?
main()


# Testing your is_perfect_square function
# Your call to main() is ignored here.
for i in [2, 4, 9, 16, 63, 64,
          65, 256, 10000, 10001]:
    if is_perfect_square(i):
        print(i)
        
