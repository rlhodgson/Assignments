
   
   
def my_enumerate(items):
    """Prints stuff"""
    return [(i,items[i]) for i in range(len(items))]

def get_column(game, col_num):
    """Returns stuff"""
    result = []
    if col_num == 0:
        a = game[0][0]
        b = game[1][0]
        c = game[2][0]
        result.append(a)
        result.append(b)
        result.append(c)
        return result
    elif col_num == 1:
        a = game[0][1]
        b = game[1][1]
        c = game[2][1]
        result.append(a)
        result.append(b)
        result.append(c)
        return result
    elif col_num == 2:
        a = game[0][2]
        b = game[1][2]
        c = game[2][2]
        result.append(a)
        result.append(b)
        result.append(c)
        return result
    
def print_even_cubes_to_number(number):
    """Prints stuff"""
    if number < 2:
        print("ERROR: number must be at least 2")
    for value in range(2, number + 1):
        if value % 2 == 0:
            cubed = value * value * value
            print("{0} * {0} * {0} = {1}".format(value, cubed))
