def isbn_dictionary(filename):
    """Returns a dictionary of a isbn number alongside a 
       tuple of author and title information"""

    try:    
        lines = open(filename).readlines()
        my_dict = {}
        for line in lines:
            line = line.strip()
            name, title, isbn_num = line.split(',')
            tup_value = (name, title)
            my_dict[isbn_num] = tup_value   
        for isbn in sorted(my_dict.keys()):
            print(isbn + ':', my_dict[isbn])
    
    except FileNotFoundError:
        print("The file {} was not found.".format(filename))
        return None
        
isbn_dictionary('.txt')
