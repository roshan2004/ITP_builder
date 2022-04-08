from vs import virtual_site1, virtual_site2
def mass_virtual(new_list, list_of):
    vs = virtual_site1(new_list) + virtual_site2(list_of)
    dc = {}
    il = []
    for i in list_of:
        for j in i:
            il.append(j)
    for i in il:
        dc[i] = 36
    
    for i in range(len(vs)):
        dc[vs[i][0]] = 0
        
    for i in range(len(vs)):
        for j, k in dc.items():
            if j in vs[i][-2:]:
                dc[j] +=18
        
    return dc