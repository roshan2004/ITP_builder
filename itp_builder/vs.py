from grouping import regroup
def virtual_site1(new_list):
    vs1 = []
    for i in range(len(new_list)):
        for j in range(len(new_list[i])):
            if len(new_list[i][j])==3:
                vs1.append([new_list[i][j][1], 1, new_list[i][j][0], new_list[i][j][2]])
    return vs1

def virtual_site2(list_of):
    vs2 = []
    attach = []
    for i in list_of:
        attach.append(regroup(i))
    for i in range(len(attach)):
        if i % 2 !=0:
            for j in range(len(attach[i])):
                if j==0: 
                    vs2.append([attach[i][j][0],1, attach[i-1][j][0], attach[i+1][j][0]])
                    vs2.append([attach[i][j][1],1, attach[i-1][j][0], attach[i+1][j][-1]])
                else:
                    if len(attach[i][j]) == 3: 

                        vs2.append([attach[i][j][1],1,attach[i-1][j][0], attach[i+1][j][-1]])
                    elif len(attach[i][j]) == 2:
                        vs2.append([attach[i][j][0],1, attach[i-1][j][0], attach[i+1][j][0]])
                        vs2.append([attach[i][j][-1],1, attach[i-1][j][-1], attach[i+1][j][-1]])
    return vs2