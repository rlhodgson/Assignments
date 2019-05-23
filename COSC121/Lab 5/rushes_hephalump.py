def num_rushes(slope_height, rush_height_gain, back_sliding):
    """Returns number of rushes needed to get to top"""
    current_height = 0
    rushes = 0 
    while current_height < slope_height:
        current_height += (rush_height_gain)
        if current_height < slope_height:
            current_height -= (back_sliding)
        rushes += 1
    return rushes

ans = num_rushes(100, 10, 0)
print(ans)