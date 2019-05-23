def row_sums(square):
    """Returns sums of lists"""
    result = []
    for row in square:
        number = len(row)
        number1 = number - 1
        total = 0            
        for nums in range(len(row)):
            total += row[nums]
            result.append(total)
        fourth_items = result[number1::number] 
    return fourth_items 

def column_sums(square):
    return [sum(i) for i in zip(*square)]

square = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
print(column_sums(square))S