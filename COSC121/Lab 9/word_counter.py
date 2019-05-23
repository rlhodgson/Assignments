def word_counter(input_str):
    """Returns a dictionary of the words and their counts in the string"""
    word_list = input_str.split(' ')
    empty = ''
    for words in word_list:
        if words == empty:
            word_list.remove(words)
    
    word_count = {}
    for word in word_list:
        word = word.lower()
        word_count[word] = word_count.get(word, 0) + 1
        
    return word_count

	
word_count_dict = word_counter(" A  a a a B B ")
print(word_count_dict)