def solution(A, B):
    answer = -1
    if A == B:
        return 0
    for i in range(len(A)):
        
        A = A[-1] + A[0:len(A)-1]
        if A==B:
            answer = i+1
            break
    
    return answer