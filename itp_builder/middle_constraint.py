def middle_constraint(new_list):
    constraints = []
    for i in new_list:
        for j in i:
            if len(j) == 2:
                constraints.append(j)
    for i in constraints:
        print(f"{i[0]}    {i[-1]}    0.21170")
        