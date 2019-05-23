def print_pair(x_coord, y_coord):
    """takes two float point coordinates and
    prints a string representation to 1dp"""
    x = x_coord
    y = y_coord
    print(("<x,y> = <{0:.1f},{1:.1f}>").format(x, y))
    
print_pair(1.72356, -22.1111)
print_pair(1.05, 3.02)