def fix_file(input_name, output_name):
    """Returns stuff"""
    infile = open(input_name)
    lines = infile.readlines()
    outfile = open(output_name, 'w')
    
    for line in lines:
        word = line.upper()
        outfile.write(word)
    infile.close()
    outfile.close()
    
ans = fix_file('test.txt', 'output.txt')
print(open('output.txt').read())