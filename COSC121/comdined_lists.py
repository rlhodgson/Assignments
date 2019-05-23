def flawed_combine(list_1, list_2):
    """Returns a new list"""
    new_list = []
    first = list_1[2:]
    last = list_2[:-2]
    new_list = first + last
    return new_list

ans = flawed_combine([10, 20, 30, 40, 50, 60], [11, 12, 13, 14, 15, 16])
print(ans)