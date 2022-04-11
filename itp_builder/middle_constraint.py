def middle_constraint(new_list, f):
    constraints = []
    for i in new_list:
        for j in i:
            if len(j) == 2:
                constraints.append(j)
    for i in constraints:
        f.write(f"{i[0]:4}    {i[-1]:4}    {1:4}    {0.21170:4}    {1000000:4}\n")
        