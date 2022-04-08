def virtual_site1(new_list):
    for i in range(len(new_list)):
        for j in range(len(new_list[i])):
            if len(new_list[i][j]) == 3:
                print(new_list[i][j][1], 1 , new_list[i][j][0], new_list[i][j][2], sep = '    ')
            

def virtual_site2(list_of):
    attach = []
    for i in list_of:
        attach.append(regroup(i))
    for i in range(len(attach)):
        if i % 2 !=0:
            for j in range(len(attach[i])):
                if j==0: 
                    print(attach[i][j][0],attach[i-1][j][0], attach[i+1][j][0])
                    print(attach[i][j][1], attach[i-1][j][0], attach[i+1][j][-1])
                else:
                    if len(attach[i][j]) == 3: 
                    
                        print(attach[i][j][1],attach[i-1][j][0], attach[i+1][j][-1])
                    elif len(attach[i][j]) == 2:
                        print(attach[i][j][0], attach[i-1][j][0], attach[i+1][j][0])
                        print(attach[i][j][-1], attach[i-1][j][-1], attach[i+1][j][-1])
        