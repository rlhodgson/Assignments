def generate_index(words_on_page):
    """Returns the inverted dictionary of the words on a page"""
    
    inverted = {}
    
    for page, words in words_on_page.items():
        for word in words:
            word = word.lower()
            if word not in inverted:
                inverted[word] = [page]
                
            else:
                inverted[word].append(page)
                
    return inverted
        
input_dict = {
   1: ['hi', 'there', 'fred'], 
   2: ['there', 'we', 'go'],
   3: ['fred', 'was', 'there']}
output_dict = generate_index(input_dict)
for word in sorted(output_dict.keys()):
    print(word + ': ' + str(output_dict[word]))