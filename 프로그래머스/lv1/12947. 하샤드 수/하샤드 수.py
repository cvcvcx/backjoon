def solution(x):    
    num_list = list(map(int,str(x)))
    div_num = sum(num_list)
    
    return True if x%div_num==0 else False