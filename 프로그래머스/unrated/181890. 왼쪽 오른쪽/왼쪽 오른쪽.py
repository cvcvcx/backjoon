def solution(str_list):
    answer = []
    l_idx = 99
    r_idx = 99
    if "l" in str_list:
        l_idx = str_list.index("l")
    if "r" in str_list:
        r_idx = str_list.index("r")
    
    if l_idx < r_idx:
        answer = str_list[:l_idx]

    elif l_idx > r_idx:
        answer = str_list[r_idx+1:]
        
    else:
        answer = []
    return answer