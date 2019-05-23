def long_enough(strings, min_length):
    """Returns if a string is long enough"""
    enough = []
    for strs in strings:
        if len(strs) >= min_length:
            enough.append(strs)
    return enough