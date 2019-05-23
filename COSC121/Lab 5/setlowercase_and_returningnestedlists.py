def set_lowercase(strings):
    """Returns the lowercase values of a set of strings"""
    for strs in range(len(strings)):
        strings[strs] = strings[strs].lower()

def board_game():
    board = [["12.3", "4.8", "4.0"], ["3", "12.7"]]
    for i in board:
        for j in i:
            return(float(j))
