def solution(array):
    answer = 0
    set_arr_list = list(set(array))
    count_arr = []
    for n in set_arr_list:
        count_arr.append(array.count(n))
    if count_arr.count(max(count_arr)) > 1:
        return -1
    else:
        answer = set_arr_list[count_arr.index(max(count_arr))]
    return answer