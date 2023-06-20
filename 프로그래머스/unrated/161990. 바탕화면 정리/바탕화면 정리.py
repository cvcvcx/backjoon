def solution(wallpaper):
    y_list = []
    x_list = []
    
    
    for i,w in enumerate(wallpaper):
        for j in range(len(w)):
            if w[j] == "#":
                y_list.append(i)
                x_list.append(j)
    #가장 작은 y에서 가장 큰 y까지
    answer = [min(y_list),min(x_list),max(y_list)+1,max(x_list)+1]
    
    #가장 작은 x에서 가장 큰 x까지
        
    
    return answer