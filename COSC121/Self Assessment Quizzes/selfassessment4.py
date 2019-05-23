def long_enough(strings, min_length):
    """Returns a list with a certain string length"""
    new_strings = []
    for word in strings:
        if len(word) >= min_length:
            new_strings.append(word)
    return new_strings

def are_anagrams(word1, word2):
    """Returns if two words are anagrams"""
    if word1 == word2:
        return False
    elif word1 != word2:
        wordone = list(word1)
        wordtwo = list(word2)
        wordone.sort()
        wordtwo.sort()
        if wordone == wordtwo:
            return True
        else:
            return False
    
def tuplinator(string):
    """Returns stuff"""
    string1 = string * 2
    string2 = string * 3
    return (string, string1, string2)

def count_messy(strings):
    """Takes a string"""
    num = 0
    for string in strings:
        if string.isalpha() == True:
            num += 1
    return num

def forth(data):
    """Returns fourth value of data"""
    return data[3]

def abs(numbers):
    """Takes a list and returns the absolute values of them"""
    for nums in range(len(numbers)):
        numbers[nums] = abs(numbers[nums])
    return numbers

def abs_nums(numbers):
    """Takes a list and returns the absolute values of them"""
    result = []
    for nums in numbers:
        nums = abs(nums)
        result.append(nums)
    return result

print(abs_nums([2, -3, -7]))