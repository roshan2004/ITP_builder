from posixpath import split


from grouping import regroup
def exclusions(list_of):
    for_excl = []
    for i in list_of:
        for_excl.append(regroup(i))
    for i in range(len(list_of)):
        if i % 2 !=0:
            for j in range(0,len(list_of[i])):
                if j == 0:
                    print(list_of[i][j], list_of[i][j+1], list_of[i-1][j+1], list_of[i-1][j], list_of[i+1][j+1], list_of[i+1][j])
                elif j == len(list_of[i])-1:
                    print(list_of[i][j], list_of[i][j-1],list_of[i-1][j-1], list_of[i-1][j], list_of[i+1][j-1], list_of[i+1][j])
                else:
                    print(list_of[i][j], list_of[i][j+1], list_of[i-1][j], list_of[i-1][j+1],list_of[i+1][j], list_of[i+1][j+1], list_of[i][j-1], list_of[i-1][j-1], list_of[i+1][j-1])
    
    for i in range(len(for_excl)):
        if i == 0:
            for j in range(len(for_excl[i])):
                if len(for_excl[i][j]) == 3:
                    print(for_excl[i][j][1], for_excl[i][j][0], for_excl[i][j][-1], *for_excl[i+1][j])
                    
        elif i == len(for_excl) - 1:
            for j in range(len(for_excl[i])):   
                if len(for_excl[i][j]) == 3:
                     print(for_excl[i][j][1], for_excl[i][j][0], for_excl[i][j][-1], *for_excl[i-1][j])