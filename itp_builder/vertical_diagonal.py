def vertical_diagonal(new_list, f):
    i = 0
    while i < len(new_list)-2:
        for j in range(len(new_list[i])):
            if len(new_list[i][j]) == 3:
                f.write(f"{new_list[i][j][0]:4}{new_list[i+1][j][::-1][0]:4}{new_list[i+1][j][::-1][1]:4}{new_list[i+2][j][-1]:4}{2:4}{180:4}{400:4}\n")
            elif len(new_list[i][j]) == 2:
                f.write(f"{new_list[i][j][0]:4}{new_list[i+1][j][::-1][0]:4}{new_list[i+1][j][::-1][1]:4}{new_list[i+2][j][-1]:4}{2:4}{180:4}{400:4}\n")
        i = i+1