def solution(arr, flag):
    answer = []
    for i,a in enumerate(arr):
        if flag[i]:
            answer += ([a]*2*a)
        elif len(answer)>0:
            answer = answer[:len(answer)-a]
    return answer