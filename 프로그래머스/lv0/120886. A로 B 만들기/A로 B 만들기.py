def solution(before, after):
    answer = 0
    for c in before:
        if before.count(c) == after.count(c):
            answer = 1
        else:
            answer = 0
            break
            
    return answer