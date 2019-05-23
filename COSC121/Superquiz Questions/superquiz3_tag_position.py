"""Written by Rachel Hodgson, 09/05/2019.
   Reads data within a given file (filename) with information about users and their donations
   to specific bands, then prints a table with a donation summary including their name, account
   status, bands and the donations to them, as well as the total number of bands and total 
   donation amount"""

import os.path

def tag_position(tag, lines):
    """Returns the position of a tag to ensure which lines are headers with name and account info,
       and which are data lines with the band and amouint info"""    
    for line in lines:
        if tag in line:
            line_index = lines.index(line)  #Index of the tag 
            return line_index            
    return -1


def tag_name_add(tag_name, lines):
    """Replaces features of the tag to meet the criteria for the tag_position function"""    
    start_tag = "<" + tag_name + ">" #changes the start tag to fit the <words> style
    end_tag = "</" + tag_name + ">" #changes the end tag to fit the </words> style
    startline = tag_position(start_tag, lines)
    endline = tag_position(end_tag, lines)
    tagged = lines[startline + 1:endline]
    return tagged   


def tag_name_start(tag_name, lines):
    """Replaces features of the tag to meet the criteria for the tag_position function"""
    start_tag_new = tag_name.replace("/", "") #changes the start tag to fit the <words> style
    startline = tag_position(start_tag_new, lines)
    endline = tag_position(tag_name, lines)
    tagged = lines[startline + 1:endline]
    return tagged   


def tagged_contents(tag_name, lines):
    """Returns the contents of a the lines between the index of the tags"""
    if "<" not in tag_name:
        tagged = tag_name_add(tag_name, lines)
        return tagged
    elif "<" in tag_name and "/" in tag_name:
        tagged = tag_name_start(tag_name, lines)
        return tagged
    elif "<" in tag_name and "/" not in tag_name:
        #replaces the tags to fit the criteria for tag_position function
        end_tag_new = tag_name.strip("<") 
        end_tagg = "</" + end_tag_new #changes the end tag to fit the </words> style
        startline = tag_position(tag_name, lines)
        endline = tag_position(end_tagg, lines)
        tagged = lines[startline + 1:endline]
        return tagged  

    
def get_filename():
    """Asks user for the filename"""
    filename = None
    while filename is None:
        filename = input("Enter a file name: ")
        if not os.path.isfile(filename): #if the file doesn't exist
            print(filename, "DOES NOT EXIST!")
            filename = None
    
    infile = open(filename, encoding="utf-8")
    lines = infile.readlines()
    infile.close()
    return lines


def process_name_status(head_lines):
    """Processes the name and status the  returns them as a tuple""" 
    _, name = head_lines[0].strip().split(':')
    _, status = head_lines[1].strip().split(':')    
    name_and_status = (name, status)
    return name_and_status

    
def get_data(data_lines):
    """Appends all the data into a list"""
    data = []
    for line in data_lines:
        _, band_name, amount = line.strip().split(',') #assigns values from the list
        amount = float(amount)
        data.append((band_name, amount))
    return data


def process_achievements(achieve_lines):
    """Returns the data for achievements then goes to the print function"""
    achieve_data = []
    for lines in achieve_lines:
        _, achievement = lines.strip().split(",")
        achieve_data.append(achievement)
    achieve_data.sort()
    print_achievements(achieve_data)


def get_total(data):
    """Returns the total donations made"""
    total = 0
    for _, amount in data:
        total += amount
    return total
   
    
def print_user_account(name, status):
    """Prints the first half of the table with a title, the name and status of the 
       user"""
    #prints first half of report
    print("-" * 40)
    print("Donation Summary")
    print("-" * 40)
    print("User name: {}".format(name.title()))
    print("Account Status: {}".format(status))   
    
    if status in ["suspended", "deleted"]:
        print("*** WARNING ***")
        print("*** User can't access their account ***")
    print("-" * 40)
   
    
def print_band_info(data, total):
    """Prints the second half od the report with band info and amounts with the 
       total contributions"""
    #prints second half of report
    for band_name, amount in sorted(data):
        print("{} ({:.2f})".format(band_name, amount))
    print("-" * 40)
    print("Count: {}".format(len(data)))
    print("Total: {:.2f}".format(total))
    print("-" * 40)    
    
    
def print_achievements(achieve_data):
    """Prints the achievement part of the report"""
    print("ACHIEVEMENTS")
    print("-" * 40)    
    to_remove = []
    for achieve in achieve_data:
        count = achieve_data.count(achieve) #counts how many times an element shows up 
        if count >= 2:
            if achieve in to_remove:
                continue
            else:
                print("{} * {}".format(achieve, count))
                to_remove.append(achieve)                
        elif count <= 1:
            print("{}".format(achieve))  
    print("-" * 40)    
   
    
def find_achieved(lines):
    """Finds out if there are any achieved tags in the given data"""
    for line in lines:
        if "achievements" in line:
            return True
    return False
   
    
def achieved(start_tag, lines):
    """Carries out the achievements process if there are achievments in the data"""
    achieve_lines = tagged_contents(start_tag, lines)
    process_achievements(achieve_lines)    


def main():
    """Runs the whole program"""
    lines = get_filename() 
    # pull out the header data
    start_tag = "<head>"   # Start tag
    head_lines = tagged_contents(start_tag, lines)
    name, status = process_name_status(head_lines)
    # pull out the data block
    start_tag = "</data>"   # Start tag
    data_lines = tagged_contents(start_tag, lines)
    data = get_data(data_lines)
    total = get_total(data)
    print_user_account(name, status)
    print_band_info(data, total)
    if find_achieved(lines) == True:
        start_tag = "achievements"
        achieved(start_tag, lines)
    
main()
