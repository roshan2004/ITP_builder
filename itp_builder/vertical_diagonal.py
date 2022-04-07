def vertical_diagonal(new_list):
    i = 0
    while i < len(new_list)-2:
        for j in range(len(new_list[i])):
            if len(new_list[i][j]) == 3:
                print(new_list[i][j][0], *new_list[i+1][j][::-1][0:2], new_list[i+2][j][-1], 2, 180, sep = '    ')
            elif len(new_list[i][j]) == 2:
                print(new_list[i][j][0], *new_list[i+1][j][::-1], new_list[i+2][j][-1], 2, 180, spe = '    ')
    i = i+1