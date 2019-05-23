import os.path 
def main(): 
    filename = None 
    while filename is None: 
        filename = input("Enter a file name: ") 
        if not os.path.isfile(filename): 
            print(filename, "DOES NOT EXIST!") 
            filename = None 
    infile = open(filename, encoding="utf-8") 
    lines = infile.readlines() 
    infile.close() # pull out the header data 
    start_tag = "" # Start tag 
    end_tag = "" # End tag 
    i = 0 
    found = False 
    while i < len(lines) and not found: 
        l = lines[i] 
        if l.strip().startswith(start_tag): 
            startline_index = i # Start line index 
            found = True 
        else: 
            i += 1 
            i = 0 
            found = False 
    while i < len(lines) and not found: 
        l = lines[i] 
        if l.strip().startswith(end_tag):
            endline_index = i # End line index 
            found = True 
        else: 
            i += 1 
    h_lines = lines[startline_index +1:endline_index] 
    _, name = h_lines[0].strip().split(':') 
    _, status = h_lines[1].strip().split(':') # pull out the data block 
    start_tag = "" # Start tag 
    end_tag = "" # End tag 
    i = 0 
    found = False 
    while i < len(lines) and not found: 
        l = lines[i] 
        if l.strip().startswith(st): 
            startline_index = i # Start line index 
            found = True 
        else: 
            i += 1 
            i = 0 
            found = False 
    while i < len(lines) and not found: 
        l = lines[i] 
        if l.strip().startswith(et): 
            endline_index = i # End line index 
            found = True 
        else: 
            i += 1 
    data_lines = lines[startline_index +1:endline_index] 
    data = [] 
    for line in data_lines: 
        _, band_name, amount = line.strip().split(',') 
        amount = float(amount) 
        data.append((band_name, amount)) 
        total = 0 
        for band_name, amount in data: 
            total += amount # Print the report 
    
    print("-" * 40) 
    print("Donation Summary") 
    print("-" * 40) 
    print("User name: {}".format(name.title())) 
    print("Account Status: {}".format(status)) 
    if status in ["suspended", "deleted"]: 
        print("*** WARNING ***") 
        print("*** User can't access their account ***") 
        print("-" * 40) 
    for band_name, amount in sorted(data): 
        print("{} ({:.2f})".format(band_name, amount)) 
        print("-" * 40) 
        print("Count: {}".format(len(data))) 
        print("Total: {:.2f}".format(total)) 
        print("-" * 40)                                 
        
main()