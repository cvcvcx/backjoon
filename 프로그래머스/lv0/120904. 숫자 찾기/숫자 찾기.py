def solution(num, k):
    answer = -1
    num_list = list(map(int,str(num)))
    if k in num_list:
        answer = num_list.index(k) +1
    return answer