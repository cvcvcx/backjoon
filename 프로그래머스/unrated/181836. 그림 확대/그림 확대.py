def solution(picture, k):
    answer = []
    result_multiply = [""]*len(picture)
    for i,p in enumerate(picture):
        for j in range(len(p)):
            result_multiply[i]+=(p[j]*k)
    
    for r in (result_multiply):
        for i in range(k):
            answer.append(r)
    
    return answer