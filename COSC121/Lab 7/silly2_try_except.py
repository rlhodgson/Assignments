def silly2(nums, indices, extra=None):
    print(len(nums), len(indices))

    new_indices = []
    for i in indices:
        if i >= 0 and i < len(nums):
            new_indices.append(i)
    #print(new_indices)
    if extra:
        new_indices.append(extra)
    print(new_indices) 
    try:
        for index in new_indices:
            #print(index, len(nums))
            if index < len(nums):
                print(nums[index])
    except IndexError:
        print("We're dead, Fred")
        
silly2([0, 0], [7, 9], -10)