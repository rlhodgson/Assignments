def get_column(game, col_num):
    """Returns the list in the coloumn asked"""
    column = []
    if col_num == 0:
        column.append(game[0][0])
        column.append(game[1][0])
        column.append(game[2][0])
    elif col_num == 1:
        column.append(game[0][1])
        column.append(game[1][1])
        column.append(game[2][1])
    elif col_num == 2:
        column.append(game[0][2])
        column.append(game[1][2])
        column.append(game[2][2])
    return column

def diagonals(game):
    """Returns the diagnols"""
    diagonal1 = [game[0][0], game[1][1], game[2][2]]
    diagonal2 = [game[0][2], game[1][1], game[2][0]]
    tupp = (diagonal1, diagonal2)
    return tupp