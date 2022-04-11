def main_dihedral(new_list, f):
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
        f.write(f'{i[0]:4}{i[1]:4}{j[0]:4}{j[1]:4}{2:4}{180:4}{400:4}\n')
            