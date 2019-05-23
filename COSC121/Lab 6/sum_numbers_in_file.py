def sum_numbers_in_file(filename):
    """Returns the numbers summed up in a file"""
    infile = open(filename)
    lines = infile.readlines()
    sumnums = []
    for line in lines:
        if line / 1 == int:
            sumnums.append(line)
    final = sum(sumnums)
    return final

ans = sum_numbers_in_file('sum_nums_test_01.txt')
print(ans)
            