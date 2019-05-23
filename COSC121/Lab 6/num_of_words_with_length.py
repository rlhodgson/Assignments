def num_words(string, length):
    """Returns stuff"""
    length = int(length)
    count = 0
    words = string.split(' ')
    for word in words:
        if len(word) == length:
            count += 1
    return count

word_count = num_words("Oh no it's a list filter!", 2)
print(word_count)

def lossy_combine(list_1, list_2):
    """Returns stuff"""
    new_list = []
    first = list_1[:-1]
    second = list_2[1:]
    new_list = first + second
    return new_list
ans = lossy_combine([10, 20, 30, 40, 50, 60], [11, 12, 13, 14, 15, 16])
print(ans)