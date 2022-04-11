from vs import virtual_site1, virtual_site2
def virtual_site(new_list, list_of, f):
    vs = virtual_site1(new_list) + virtual_site2(list_of)
    for i in vs:
        f.write(f"{i[0]:4}{i[1]:4}{i[2]:4}{i[3]:4}\n")