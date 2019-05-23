def find_key(input_dict, value):
    """Returns the key of that value in the dict"""
    value_key = {}
    
    for key, val in input_dict.items():
        value_key[val] = key
        
    if value in value_key:
        input_key = value_key[value]
        return input_key
    else:
        return None

test_dictionary = {100:'a', 20:'b', 3:'c', 400:'d'}
print(find_key(test_dictionary, 'e'))