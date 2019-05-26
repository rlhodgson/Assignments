import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

"""This is a program that takes a filename as a  parameter containing information
   about albums. It should prompt the user for a filename, read the information into
   lines, extract the information into a library and then print it in a formatted
   table.
   Author: Rachel Hodgson
   Date: 25-05-2019
"""
import os.path #used to check the validity of the filename when prompted
import matplotlib.pyplot as plt


class Album:
    """Stores the information about an album"""
    def __init__(self, album_id, name, band, cost):
        """The data that forms an album, note that:
        - album_id is a int
        - cost is a float
        - the rest are strings
        """
        self.album_id = album_id
        self.name = name
        self.band = band
        self.cost = cost
        self.total_sold = 0 
        self.certificate = ""
        
        
    def add_to_sold(self, count):
        """Adds to the internal album counter of the album"""
        if count >= 0:
            self.total_sold += count
            return self.total_sold
        else:
            template = "Attempt to add {} to Album: {}. VALUE MUST NOT BE NEGATIVE"
            raise ValueError(template.format(count, self.album_id))  
        
        
    def add_certificate(self):
        """Taks the total sold and returns a status level"""
        status = int(self.total_sold)
        if status < 50000:
            self.certificate = ""
        elif status >= 50000 and status < 100000:
            self.certificate = "Gold"
        elif status >= 100000 and status < 500000:
            self.certificate = "Platinum"
        elif status >= 500000:
            self.certificate = "Diamond"
    
    
    def __repr__(self):
        """Creates the string function needed to return the correct values to 
           the function by making it a string so it can be represented, in this
           case it is only the name because that is all required so far"""
        return ("{:<5}{:<30}{:>10}{:>15}".format(self.album_id, self.name, self.total_sold, 
                                                 self.certificate))
        

def get_filename():
    """Asks user for the filename"""
    filename = None
    while filename is None:
        filename = input("Enter a data file name: ")
        if not os.path.isfile(filename): #if the file doesn't exist
            print("Invalid File Name Entered!")
            filename = None
    
    infile = open(filename)
    lines = infile.readlines()
    infile.close()
    return (lines, filename)

        
def extract_album(lines, index):
    """Takes a set of lines as a parameter and an index for the lines and returns 
       the information in the lines on an album using the __str__ function in Album"""
    for line in lines[index:]:
        line = line.strip()
        albumid = int((lines[index + 1]).strip())
        name = (lines[index + 2]).strip()
        band = (lines[index + 3]).strip()
        cost = float((lines[index + 4]).strip())
        return Album(albumid, name, band, cost) #makes all info possible class attributes
    
    
def extract_all_albums(lines):
    """Takes a list of lines as a parameter containing information on an album.
       Returns the album information as a dictionary comparing the album id to 
       the relveant information on the albums."""
    album_dict = {}
    for index, line in enumerate(lines):
        if line.startswith("<a"):
            line_index = int(index)
            line = line.strip()
            albumid = int((lines[index + 1]).strip())
            album_classed = extract_album(lines, line_index)
            album_dict[albumid] = album_classed #assigns the key(id) to the values
    return album_dict
        
        
def read_sales(lines, albums):
    """Reads the sales files and runs the add_to_sold function on the album data
       that has ahd sales as shown in the sales tags. Then returns the albums
       dictionary again with the updated sales ready to print the table"""
    start_index = None
    end_index = None
    for line in lines:
        if line.startswith("<s"):
            start_index = int(lines.index(line)) #finding the start and end indexes
        elif line.startswith("</s"):
            end_index = int(lines.index(line))
    if start_index == None and end_index == None:
        pass
    elif start_index != None and end_index != None:
        sales_lines = lines[start_index + 1:end_index]
        for line in sales_lines:
            _, albumid, sold = line.split(",") #splits up the data lines
            for album_id, albuminfo in albums.items():
                if int(album_id) == int(albumid):
                    albuminfo.add_to_sold(int(sold)) #adds all the sold amounts of albums 
                albuminfo.add_certificate() #adds the certificate based on the totals
    return albums


def total_sold(album):
    """Helper function that returns total_sold to enable the sort key which 
       has to be a function"""
    return album.total_sold


def print_graph(sorted_albums, total_sales):
    """Prints our the sales bar graph portion of the program"""
    for album in sorted_albums:
        percentage = (100 / int(total_sales)) * int(album.total_sold)
        percentage = int(percentage)
        lines = "=" * int(percentage)
        print("{:>4}{:>5}% {}".format(album.album_id, percentage, lines))

def print_matplotlib(sorted_albums, total_sales):
    total_sales = int(total_sales)
    data = []
    for album in sorted_albums:
        percentage = (100 / int(total_sales)) * int(album.total_sold) 
        album_id = album_id # Some random numbers for testing
        data.append(percentage)
    
    axes = plt.axes()
    axes.bar(range(total_sales), data, tick_label=album_id)
    axes.set_title("Album Sales Summary 'filename'")
    axes.set_xlabel("Album ID")
    axes.set_ylabel("Percent of Total Sales")
    plt.show()    

def print_table(album_dict, filename):
    """Prints the information from the functions into a formatted table"""
    print()
    print("Album Catalogue Summary")
    print("-" * 60)
    print('{:<5}{:<30}{:>10}{:>15}'.format("ID", "ALBUM NAME", "# SOLD", "CERTIFICATE"))
    sorted_albums = sorted(album_dict.values(), key=total_sold, reverse=True)
    for album in sorted_albums:
        print(album)
    print()
    print("Sales Bar Graph")
    print("-" * 30)
    print("  {:<4}{:>5}".format("ID", "Freq Graph"))
    total_sales = 0
    for album in sorted_albums:
        total_sales += int(album.total_sold)
    print_graph(sorted_albums, total_sales)
    make_barchart(album_dict, sorted_albums, filename, total_sales)
    
def make_barchart(album_dict, sorted_albums, filename, total_sales): 
    albumids = []
    for albumid, albums in album_dict:
        albums.append(albumid)
    
    albumids = tuple(albumids)
    y_pos = np.arange(len(albumids))
    percentage = []
    
    for album in sorted_albums:
        percent = (100 / int(total_sales)) * int(album.total_sold)
        percent = int(percent)
        percentage.append(percent)
    
    plt.bar(y_pos, percentage, align='center', alpha=0.5)
    plt.xticks(y_pos, albumids)
    plt.ylabel('Percentage of total sales')
    plt.xlabel('Album ID')
    plt.title('Album sales summary ({})'.format(filename))
    
    plt.show()
    

def main():
    """Runs the main code"""
    lines, filename = get_filename()
    album_dictionary = extract_all_albums(lines)
    album_dictionary = read_sales(lines, album_dictionary)
    print_table(album_dictionary, filename)
    
main()
