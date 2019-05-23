def first_half(s):
    """Taks a string and returns the first half"""
    if len(s) % 2 == 0:
        num = len(s) / 2
        num = int(num)
        first = s[0:num]
        return first
    elif len(s) % 2 != 0:
        s_str = s[:-1]
        num = len(s_str) / 2
        num = int(num)
        sec = s_str[0:num]
        return sec

def first_two(s):
    """Takes a string and returns the first 2 letters"""
    if len(s) >= 2:
        string = s[0:2]
        return string
    elif len(s) < 2:
        return s
    
def hello_name(s):
    """Takes a string and returns hello and the string"""
    to_return = "Hello {}!".format(s)
    return to_return

def left2(s):
    """Takes and a string and returns it with rotated letters"""
    first_two = s[0:2]
    rest = s[2:]
    rotated = rest + first_two
    return rotated

def make_1221(str1, str2):
    """Takes two strings and repeats the strings"""
    final = str1 + str2 + str2 + str1
    return final

def make_out_word(out, word):
    """Returns the word inside the out thing"""
    num = int(len(out) / 2)
    first = out[0:num]
    last = out[num:]
    final = first + word + last
    return final

def make_tags(tag, word):
    """Returns the word in the tags"""
    tag1 = "<{}>".format(tag)
    tag2 = "</{}>".format(tag)
    final = tag1 + word + tag2
    return final

def non_start(str1, str2):
    """Returns strings together with first letter removed"""
    one = str1[1:]
    two = str2[1:]
    final = one + two
    return final

def swap_ends(s):
    """Takes string and returns it witht eh first and last letter swapped"""
    first = s[0]
    last = s[-1]
    mid = s[1:-1]
    final = last + mid + first
    return final

def swap_halves(s):
    """Takes string and returns a string made of second half"""
    if len(s) % 2 == 0:
        f_index = int(len(s) / 2)
        first = s[0:f_index]
        second = s[f_index:]
        final = second + first
        return final
    elif len(s) % 2 != 0:
        num = int((len(s) - 1) / 2)
        first = s[0:num]
        second = s[num:]
        final = second + first
        return final
    
def without_end(s):
    """Returns a version of a string without the first two letters"""
    string = s[1:-1]
    return string