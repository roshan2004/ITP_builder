def exclusions(list_of):
    for i in range(len(list_of)):
        if i % 2 !=0:
            for j in range(0,len(list_of[i])):
                if j == 0:
                    print(list_of[i][j], list_of[i][j+1], list_of[i-1][j+1], list_of[i-1][j], list_of[i+1][j+1], list_of[i+1][j])
                elif j == len(list_of[i])-1:
                    print(list_of[i][j], list_of[i][j-1],list_of[i-1][j-1], list_of[i-1][j], list_of[i+1][j-1], list_of[i+1][j])
                else:
                    print(list_of[i][j], list_of[i][j+1], list_of[i-1][j], list_of[i-1][j+1],list_of[i+1][j], list_of[i+1][j+1], list_of[i][j-1], list_of[i-1][j-1], list_of[i+1][j-1])
        
        