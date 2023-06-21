def solution(num_list):
    answer = 0
    for num in num_list:
        tmp = num
        while tmp != 1:
            answer += 1
            tmp = int(tmp//2) if tmp % 2 == 0 else int((tmp-1) // 2)
    return answer