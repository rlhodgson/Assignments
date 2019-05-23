def max_num_from_file(filename):
    """Returns max value"""
    infile = open(filename)
    lines = infile.readlines()
    maxnum = 0 
    for vals in lines:
        vals = int(vals)
        if vals > maxnum:
            maxnum = vals
    return maxnum
            
ans = max_num_from_file('test01.txt')
print(ans)