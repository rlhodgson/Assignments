def get_name(name_dict, id_num):
    """Returns the name associated with an id number"""
    if id_num in name_dict:
        name = name_dict[id_num]                     
        return name
    else:
        return None
        
test_dictionary = {11:'Fred', 2001:'Agnes'}
ans = get_name(test_dictionary, 2002)
print(ans)