def generate_daily_totals(input_filename, output_filename):
    """Generates the totals to another file"""
    infile = open(input_filename)
    lines = infile.readlines()
    outfile = open(output_filename, "w")
    for line in lines:
        summ = 0
        pieces = line.split(",")
        date = pieces[0]
        nums = pieces[1:]
        for num in nums:
            num = float(num)
            summ += num
        final = ("{0} = {1:.2f}\n".format(date, summ))
        outfile.write(final)
    infile.close()
    outfile.close()
    
import os.path
generate_daily_totals('data63.txt', 'marks2.txt')
if not os.path.exists('marks2.txt'):
    print("You don't seem to have created the required output file!")
else:
    print(open('marks2.txt').read())