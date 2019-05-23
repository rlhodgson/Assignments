"""Print all the perfect squares from zero up to a given maximum.
   This version is refactored to make it more understandable
   and more maintainable."""

def read_bound(message):
    """Reads the upper bound from the standard input (keyboard).
       If the user enters something that is not a positive integer
       the function issues an error message and retries
       repeatedly"""
    
    # WHAT GOES HERE?
    limit = None
    while limit == None:
        num_limit = input(message)
        if num_limit.isnumeric():
            limit = int(num_limit)
        else:
            print("You must enter a positive number.")
    return limit



def is_perfect_square(num):
    """Return true if and only if num is a perfect square"""
    
    # AND WHAT GOES HERE?
    import math
    nums = math.sqrt(num)
    rounded_num = round(nums, 1)
    if nums == rounded_num:
        return True

def print_squares(lower_bound, upper_bound, squares):
    """Print a given list of all the squares up to a given upper bound"""
    
    # AND WHAT GOES HERE?
    print("The perfect squares from {} to {} are: ".format(lower_bound, upper_bound))
    for square in squares:
        print(square, end=' ')
    print()

    
def main():
    """Every home should have one"""
    lower_bound = read_bound("Enter the lower bound: ")
    upper_bound = read_bound("Enter the upper bound: ")
    squares = []
    for num in range(lower_bound, upper_bound + 1):
        if is_perfect_square(num):
            squares.append(num)

    print_squares(lower_bound, upper_bound, squares)


main()