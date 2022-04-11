def short_diag_bond(new_list, f):
    short_diag_1 = []
    short_diag_2 = []

    for i in range(len(new_list)):
        if i == len(new_list)-1:
            continue
        for j in new_list[i]:
            if len(j) == 2:
                short_diag_1.append(j[0])
            
    for i in range(len(new_list)):
        if i == 0:
            continue
        for j in new_list[i]:
            if len(j) == 2:
                short_diag_2.append(j[-1])
            
    
    for index1, index2 in zip(short_diag_1, short_diag_2):
        f.write(f"{index1:4}    {index2:4}    {1:4}    {0.53627:4}\n")
    