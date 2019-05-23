def print_nth_value(data, n):
    """Prints the index n value in data"""
    n = int(n)
    try:
        print(data[n])
    except:
        print("Invalid position provided")