def solution(my_string):
    split_list = list(my_string.split())
    answer = int(split_list[0])
    
    for i in range(1,len(split_list)):
        if split_list[i].isdigit():
            if split_list[i-1] == "+":
                answer += int(split_list[i])
            else:
                answer -= int(split_list[i])
    return answer