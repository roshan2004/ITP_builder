def bond_core(new_list, f):
        core_i = []
        core_j = []
        for i in range(len(new_list)):
            for j in new_list[i]:
                if len(j) == 3:
                    core_i.append(j[0])
                    core_j.append(j[-1])
        for id1, id2 in zip(core_i, core_j):
            f.write(f"{id1:4}     {id2:4}    {1:4}    {0.47324:4}\n")
    