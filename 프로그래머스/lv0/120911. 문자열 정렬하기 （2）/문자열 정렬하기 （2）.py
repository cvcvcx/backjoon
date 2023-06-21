def solution(my_string):
    answer = ''
    my_string = my_string.lower()
    for s in sorted(my_string):
        answer += s
    return answer