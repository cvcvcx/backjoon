def solution(n):
    answer = 0
    number_list = list(map(int,str(n)))
    number_list.sort()
    number_list = number_list[::-1]
    str_num = ""
    for num in number_list:
        str_num += str(num)
        answer = int(str_num)
    return answer