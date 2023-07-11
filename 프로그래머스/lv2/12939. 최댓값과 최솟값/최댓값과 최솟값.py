def solution(s):
    answer = ''
    str_list = list(map(int,s.split()))
    str_list.sort()
    answer = f"{str_list[0]} {str_list[-1]}"
    return answer