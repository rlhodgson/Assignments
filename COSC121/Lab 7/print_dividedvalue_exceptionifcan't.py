def print_nth_item_divided(data, n, divisor):
    """Prints the nth index in data divided by something"""
    try:
        print(data[n]/divisor)
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except TypeError:
        print("Parameters must be numbers.")
    except IndexError:
        print("Invalid position provided.")