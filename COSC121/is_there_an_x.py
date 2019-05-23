def x_at_either_end(string):
    """Return true or false if a word begins or ends with 'x'"""
    if string.startswith("x"):
        is_there_x = True
    elif string.endswith("x"):
        is_there_x = True
    else:
        is_there_x = False
    return(is_there_x)

print(x_at_either_end('xang'))
print(x_at_either_end('nax'))
print(x_at_either_end('lin'))