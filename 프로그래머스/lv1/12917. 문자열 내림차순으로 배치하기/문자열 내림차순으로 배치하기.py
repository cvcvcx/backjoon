def solution(s):
    answer = ""
    str_list = list(s)
    str_list.sort(reverse=True)
    for s in str_list:
        answer += s    
    return answer