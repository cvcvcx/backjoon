def solution(A, B):
    answer = 0
    for i in range(len(A)):
        if B == A:
            break
        answer += 1
        A = A[-1]+A[:len(A)-1]
    if A != B:
        return -1
    return answer