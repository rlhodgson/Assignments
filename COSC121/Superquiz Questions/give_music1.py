"""Reads data within a given file (filename) with information about users and their donations
   to specific bands, then prints a table with a donation summary including their name, account
   status, bands and the donations to them, as well as the total number of bands and total 
   donation amount"""

import os.path
def main():
    """Runs the whole program"""
    filename = None
    while filename is None:
        filename = input("Enter a file name: ")
        if not os.path.isfile(filename): #if the file doesn't exist
            print(filename, "DOES NOT EXIST!")
            filename = None
    
    infile = open(filename, encoding="utf-8")
    lines = infile.readlines()
    infile.close()
    
    # pull out the header data
    start_tag = "<head>"   # Start tag
    end_tag = "</head>"  # End tag
    i = 0
    found = False
    while i < len(lines) and not found:
        new_line = lines[i]
        if new_line.strip().startswith(start_tag): #works out if it is a header
            startline = i  # Start line index
            found = True
        else:
            i += 1
    
    i = 0
    found = False
    while i < len(lines) and not found:
        new_line = lines[i]
        if new_line.strip().startswith(end_tag):
            endline = i  # End line index
            found = True
        else:
            i += 1
    
    
    h_lines = lines[startline +1:endline]
    _, name = h_lines[0].strip().split(':')
    _, status = h_lines[1].strip().split(':')
    
    
    
    # pull out the data block
    start_tag = "<data>"   # Start tag
    end_tag = "</data>"  # End tag
    i = 0
    found = False
    while i < len(lines) and not found:
        new_line = lines[i]
        if new_line.strip().startswith(start_tag): #works out if it is data
            startline = i  # Start line index
            found = True
        else:
            i += 1
    
    i = 0
    found = False
    while i < len(lines) and not found:
        new_line = lines[i]
        if new_line.strip().startswith(end_tag):
            endline = i  # End line index
            found = True
        else:
            i += 1
    
    
    data_lines = lines[startline+1:endline]
    data = []
    for line in data_lines:
        _, band_name, amount = line.strip().split(',') #assigns values from the list
        amount = float(amount)
        data.append((band_name, amount))
    
    total = 0
    for band_name, amount in data:
        total += amount
    
    
    # Print the report
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
