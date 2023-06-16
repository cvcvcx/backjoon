def solution(left, right):
    answer = 0
    number_list = list(range(left,right + 1))
    for num in number_list:
        count = 0
        for n in range(1,num+1):
            if num % n == 0:
                count += 1
        if count % 2 == 0:
            answer += num
        else:
            answer -= num
    return answer