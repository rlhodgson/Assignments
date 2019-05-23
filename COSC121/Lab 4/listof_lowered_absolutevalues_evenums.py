def lower_case(strings):
    """Returns strings as a lower case"""
    lowered = []
    for strs in strings:
        strs = strs.lower()
        lowered.append(strs)
    return lowered

def abs_nums(numbers):
    """Returns the absolute values of a list"""
    final = []
    for nums in numbers:
        nums = abs(nums)
        final.append(nums)
    return final
    
def evens(numbers):
    """Returns the even numbers"""
    even_nums = []
    for nums in numbers:
        if nums % 2 == 0:
            even_nums.append(nums)
    return even_nums