def make_stats(filename):
    """Returns stats of data"""
    infile = open(filename)
    lines = infile.readlines()
    listofnums = []
    for line in lines:
        nums = line.split(":")
        for val in nums:
            val = float(val)
            listofnums.append(val)
        maxi = max(listofnums)
        mini = min(listofnums)
        summ = sum(listofnums)
        avg = summ / len(listofnums)
        tup = (maxi, mini, avg)
    infile.close()
    return tup

(maximum, minimum, average) = make_stats('day_temps.txt')
print("({0:.5}, {1:.5}, {2:.5})".format(maximum, minimum, average))