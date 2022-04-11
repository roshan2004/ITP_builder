def side_left(list_of, f):
    side_left = []
    for i in range(len(list_of)):
        if i % 2 == 0:
            side_left.append(list_of[i][0])
    sides = [side_left[i:i+2] for i in range(len(side_left)) if len(side_left[i:i+2]) == 2]
    for i in sides:
        f.write(f'{i[0]:4}    {i[-1]:4}    {1:4}    {0.52798:4}\n')