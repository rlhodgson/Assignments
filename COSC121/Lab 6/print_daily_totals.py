def print_daily_totals(filename):
    """Returns the reversed value"""
    infile = open(filename)
    lines = infile.readlines()
    for line in lines:
        summ = 0
        pieces = line.split(",")
        date = pieces[0]
        nums = pieces[1:]
        for num in nums:
            num = float(num)
            summ += num
        print(date, "=", '{0:.2f}'.format(summ))
            