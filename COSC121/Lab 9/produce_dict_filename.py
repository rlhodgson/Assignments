def produce_dictionary(filename):
    """Returns a dictionary of all the keys and their counts from a given filename"""
    infile = open(filename)
    lines = infile.readlines()
    
    word_count = {}
    
    for word in lines:
        word = word.lower()
        word = word.strip()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
            
    empty = ''
    if empty in word_count:
        word_count.pop(empty)
        
    return word_count

dictionary = produce_dictionary('empty.txt')
for key in dictionary:
    print(key + ': ' + str(dictionary[key]))