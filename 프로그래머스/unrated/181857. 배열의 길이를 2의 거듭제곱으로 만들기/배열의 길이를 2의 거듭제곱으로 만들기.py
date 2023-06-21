def solution(arr):
    answer = []
    len_num = 0
    for i in range(11+1):
        if len(arr)<=2**i:
            len_num = 2**i
            break
            
    for j in range(len_num):
        if j<len(arr):
            answer.append(arr[j])
        else:
            answer.append(0)
    return answer