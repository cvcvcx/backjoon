def solution(my_string, n):
    answer = ''
    str_list = list(my_string)
    for s in str_list:
        answer += s*n
    return answer