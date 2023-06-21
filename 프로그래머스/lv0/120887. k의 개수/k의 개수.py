def solution(i, j, k):
    answer = 0
    str_list = list(map(str,range(i,j+1)))
    for s in str_list:
        for n in s:
            if n == str(k):
                answer += 1
            
    return answer