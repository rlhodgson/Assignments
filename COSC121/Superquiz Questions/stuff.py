"""This is a program that takes a filename as a  parameter containing information
   about albums. It should prompt the user for a filename, read the information into
   lines, extract the information into a library and then print it in a formatted
   table.
   Author: Rachel Hodgson
   Date: 21-05-2019
"""
import os.path #used to check the validity of the filename when prompted

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
        
    def add_to_sold(self, count):
        """Adds to the internal album counter of the album"""
        if count >= 0:
            self.total_sold += count
        else:
            template = "Attempt to add {} to Album: {}. VALUE MUST NOT BE NEGATIVE"
            raise ValueError(template.format(count, self.album_id))    
        
    def __str__(self):
        """Creates the string function needed to return the correct values to 
           the function by making it a string so it can be represented, in this
           case it is only the name because that is all required so far"""
        output = ("{:<30}{:>10}".format(self.name, self.total_sold))
        return output
   
        
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
    return lines

        
def extract_album(lines, index):
    """Takes a set of lines as a parameter and an index for the lines and returns 
       the information in the lines on an album using the __str__ function in Album"""
    for line in lines[index:]:
        line = line.strip()
        albumid = int((lines[index + 1]).strip())
        name = (lines[index + 2]).strip()
        band = (lines[index + 3]).strip()
        cost = float((lines[index + 4]).strip())
        return Album(albumid, name, band, cost)
    
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
            album_dict[albumid] = album_classed
    return album_dict
        
def print_table(album_dict):
    """Prints the information from the functions into a formatted table"""
    print()
    print("Album Catalogue Summary")
    print("-" * 45)
    print('{:<5}{:<30}{:>10}'.format("ID", "ALBUM NAME", "# SOLD"))
    for albumid, albuminfo in sorted(album_dict.items()): #must be sorted for the correct order
        albumid = str(albumid)
        albuminfo = str(albuminfo)
        print('{:<5}{:<30}'.format(albumid, albuminfo))
        
def read_sales(lines, albums):
    """Reads the sales files and runs the add_to_sold function on the album data
       that has ahd sales as shown in the sales tags. Then returns the albums
       dictionary again with the updated sales ready to print the table"""
    start_index = None
    end_index = None
    for line in lines:
        if line.startswith("<s"):
            start_index = int(lines.index(line))
        elif line.startswith("</s"):
            end_index = int(lines.index(line))
    if start_index == None and end_index == None:
        pass
    elif start_index != None and end_index != None:
        sales_lines = lines[start_index + 1:end_index]
        for line in sales_lines:
            _, albumid, sold = line.split(",")
            for album_id, albuminfo in albums.items():
                if int(album_id) == int(albumid):
                    albuminfo.add_to_sold(int(sold))
    return albums
        
        
        
    
def main():
    """Runs the main code"""
    lines = get_filename()
    album_dictionary = extract_all_albums(lines)
    album_dictionary = read_sales(lines, album_dictionary)
    print_table(album_dictionary)
    
main()