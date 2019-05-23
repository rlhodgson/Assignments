def print_gymnastic_score(mark_gained, maximum=70):
    """Prints a string displaying the score"""
    percent = (100 / maximum) * mark_gained
    mark = mark_gained
    maxx = maximum
    print("Your score: {0:.1f}/{1:.1f} ({2:.1f}%)".format(mark, maxx, percent))


"""Demo of keyword arguments. """
        