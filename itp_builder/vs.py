def virtual_site1(new_list):
    for i in range(len(new_list)):
        for j in range(len(new_list[i])):
            if len(new_list[i][j]) == 3:
                print(new_list[i][j][1], 1 , new_list[i][j][0], new_list[i][j][2], sep = '    ')
            

def virtual_site2(list_of):
    for i in range(len(list_of)):
        if i % 2 !=0:
            for j in range(len(list_of[i])):
                print(list_of[i][j], 1, list_of[i-1][j], list_of[i+1][j])
                
