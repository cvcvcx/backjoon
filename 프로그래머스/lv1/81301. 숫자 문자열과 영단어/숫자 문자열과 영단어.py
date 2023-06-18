def solution(s):
    str_num_list = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    
    for i,str_num in enumerate(str_num_list):
        if str_num in s:
            s = s.replace(str_num, str(i))
    
    return int(s)