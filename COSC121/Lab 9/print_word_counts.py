def print_word_counts(filename):
    """Prints the word followed by its occurence from a 
       given filename, printed one word per line follwed 
       by the count in alphabetical order"""
    import re
    
    input_file = open(filename, 'r')
    source_string = input_file.read().lower()
    input_file.close()
    words = re.findall('[a-zA-Z]+', source_string)
    
    word_count = {}
    
    for word in words:
        word.lower()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
            
    for key in sorted(word_count):
        print(key + ': ' + str(word_count[key]))    
    
print_word_counts('empty.txt')