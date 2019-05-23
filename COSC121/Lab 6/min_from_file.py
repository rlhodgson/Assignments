def min_num_from_file(filename):
    """Returns smallest value"""
    infile = open(filename)
    lines = infile.readlines()
    lisst = []
    for num in lines:
        lisst.append(num)
    minnum = min(lisst)
    return minnum

answer = min_num_from_file('test01.txt')
print(answer)