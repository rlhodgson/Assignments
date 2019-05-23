def character_set_counts(string_1, string_2, string_3):
    """Returns the number of characters that are in string1 and in string2 but
       not in string3"""
    string1 = set(string_1)
    string2 = set(string_2)
    string3 = set(string_3)
    
    string1_2 = string1.intersection(string2)
    
    not_string3 = string1_2.difference(string3)
    
    return (len(not_string3))

answer = character_set_counts('abcdef', 'bcd', 'ace')
print(answer)
  