def solution(food):
    answer = ''
    str_num_list = []    
    for i,f in enumerate(food):
        if i != 0:
            str_num_list.append(int(f)//2)
    for i,num in enumerate(str_num_list):
        
        answer += str(i+1)*num
    answer = answer + "0" + answer[::-1]
    return answer