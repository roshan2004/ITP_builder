def main_dihedral(new_list):
    first = []
    second = []
    for i in range(len(new_list)-1):
        for m in new_list[i]:
            if len(m) == 3:
                first.append(m[::-1][0:3:2])
            elif len(m) == 2:
                first.append(m[::-1])
                
    for i in range(1, len(new_list)):
        for m in new_list[i]:
            if len(m) == 3:
                second.append(m[::-1][0:3:2])
            elif len(m) == 2:
                second.append(m[::-1])
                
    for i, j in zip(first, second):
        print(*i, *j, 180, sep = '    ')
            
