def solution(num_list, n):
    answer = []
    dis_idx_dict = {}
    idx_num_dict = {}
    
    for i,num in enumerate(num_list):
        idx_num_dict[i] = num
        if abs(num-n) in dis_idx_dict:
            dis_idx_dict[abs(num - n)].append(i)
        else:
            dis_idx_dict[abs(num - n)] = [i]
    
    dis_list = list(dis_idx_dict.keys())
    dis_list.sort()
    
    for dis in dis_list:
        tmp_list = [idx_num_dict[i] for i in dis_idx_dict[dis]]
        tmp_list.sort(reverse=True)
        answer += tmp_list
        
    return answer