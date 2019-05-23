def get_filename():
    """Gets the filename and lines"""
    filename = input()
    lines = open(filename).readlines()
    return lines

def get_indexes(lines):
    s = lines.index('<begin step data>\n')
    e = lines.index('<end step data>\n', s + 1)
    index = (s, e)
    return index

def initial_steps(lines, start_index, end_index):
    for line in lines[start_index + 1 : end_index]:
        steps = line.strip().split(',')
    return steps

    
def total_steps(steps):
    t = 0
    sum = 0
    for step_string in steps:
        sum = sum + int(step_string)
        t += sum
    return t    

def print_total(total_steps):
    print("Total steps:", t)    
    
def main():
    """Runs the program"""
    lines = get_filename()
    start_index, end_index = get_indexes(lines)
    steps = initial_steps(lines, start_index, end_index)
    total_steps = total_steps(steps)
    print_total(total_steps)
main()