def solution(my_string, m, c):
    answer_list=[""]*m
    for i in range(len(my_string)):
        answer_list[i%m]+=(my_string[i])
    return answer_list[c-1]