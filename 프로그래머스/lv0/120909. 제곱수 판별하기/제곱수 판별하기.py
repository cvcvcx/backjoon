def solution(n):
    answer = 2
    if n**0.5 % 1 == 0:
        answer = 1
    
    return answer