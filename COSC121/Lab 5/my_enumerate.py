def my_enumerate(items):
    """Returns a tuple of the item and index"""
    items = list(items)
    result = []
    for values in range(len(items)):
        tupp = (values, items[values])
        result.append(tupp)    
    return(result)