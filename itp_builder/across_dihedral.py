def across_dihedral(new_list, f):
    a_list = []
    b_list = []
    middle1 = []
    middle2 = []
    for i in range(len(new_list)-1):
        for m in new_list[i]:
            if len(m) == 3:
                middle1.append(m[::][0:3:2])
            elif len(m) == 2:
                middle1.append(m[::-1])
    
    for i in range(1, len(new_list)):
        for m in new_list[i]:
            if len(m) == 3:
                middle2.append(m[::-1][0:3:2])
            elif len(m) == 2:
                middle2.append(m[::-1])
    
    
    ab = list(zip(middle1, middle2))
    
    for i in range(len(ab)):
        if i %2 == 0:
            a_list.append([ab[i][0][0], ab[i][1][0]])
        else:
            b_list.append([ab[i][0][1], ab[i][1][0]])
            
            
    for i, j in zip(a_list, b_list):
        f.write(f'{i[0]:4}{i[1]:4}{j[0]:4}{j[1]:4}{2:4}{180:4}{400:4}\n')
    