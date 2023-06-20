def solution(my_string, indices):
    answer = ""
    list_my_string = list(my_string)
    for i in indices:
        list_my_string[i] = " "
    for s in list_my_string:
        if s != ' ':
            answer += s
    return answer