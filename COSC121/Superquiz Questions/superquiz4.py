"""This is a program that takes information and uses it in the Album class to 
   show the info and calculate values based on futher info given 
   Author: Rachel Hodgson
   Date: 20-05-2019
"""

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
        output = ""
        output += "Album Name: {}\n".format(self.name)
        output += "Band: {}\n".format(self.band)
        output += "Purchase Price: ${:.2f}".format(self.cost)
        return output
    
    def __repr__(self):
        return "<<{}>>".format(self.album_id)
    
        
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

file = open('album0.txt')
content = file.read()
file.close()
lines = content.splitlines()

albums = extract_all_albums(lines)
print(albums)
    
