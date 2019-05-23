def get_filename():
    """Gets the filename and lines"""
    filename = input()
    lines = open(filename).readlines()
    return lines

def get_indexes(lines):
    start = lines.index('<begin step data>\n')
    end = lines.index('<end step data>\n', start + 1)
    index = (start, end)
    return index

def total_steps(lines, start_index, end_index):
    total = 0
    for line in lines[start_index + 1 : end_index]:
        step = line.strip().split(',')
        for num in step:
            total += int(num)
    return total
   
def print_total(inital_steps):
    print("Total steps:", inital_steps)    
    
def main():
    """Runs the program"""
    lines = get_filename()
    start_index, end_index = get_indexes(lines)
    steps = total_steps(lines, start_index, end_index)
    print_total(steps)
main()