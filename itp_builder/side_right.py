def side_right(list_of, f):
    side_right = []
    for i in range(len(list_of)):
        if i % 2 == 0:
            side_right.append(list_of[i][-1])
    sides = [side_right[i:i+2] for i in range(len(side_right)) if len(side_right[i:i+2]) == 2]
    for i in sides:
        f.write(f'{i[0]:4}    {i[-1]:4}    {1:4}    {0.52798:4}\n')