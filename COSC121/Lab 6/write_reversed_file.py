def write_reversed_file(input_filename, output_filename):
    """Returns info to a seperate file"""
    infile = open(input_filename)
    strings = infile.readlines()
    outfile = open(output_filename, "w")
    rev_strings = reversed(strings)
    for string in rev_strings:
        outfile.write(string)
    infile.close()
    outfile.close()
    
    import os.path
    write_reversed_file('data.txt', 'reversed1.txt')
    if not os.path.exists('reversed1.txt'):
        print("You don't seem to have created the required output file!")
    else:
        print(open('reversed1.txt').read())    