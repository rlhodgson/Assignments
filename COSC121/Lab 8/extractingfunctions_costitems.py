def fun_function(n_items, cost_per_item, discount_percent, discount_threshold):
    """Returns the total cost"""
    cost = n_items * cost_per_item                  # line 1
    if n_items > discount_threshold:                # line 2
        cost = cost * (1 - discount_percent / 100)  # line 3
    return cost

def main():
    """Compute and print the total cost of a number of items"""

    # First initialise all variables
    cost_per_item = 27      # Without discount
    discount_percent = 10
    discount_threshold = 20

    # Get the number of items to be priced.
    n_items = int(input("How many items? "))

    # Now compute the total cost
    cost = fun_function(n_items, cost_per_item, discount_percent, discount_threshold)

    # Print the results
    print('{} items cost ${:.2f}'.format(n_items, cost))

main()