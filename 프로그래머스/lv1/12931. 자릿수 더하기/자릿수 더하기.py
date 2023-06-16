def solution(n):
    num_list = list(map(int,list(str(n))))
    answer = 0
    for num in num_list:
        answer += num

    return answer