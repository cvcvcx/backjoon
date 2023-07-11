# A와 B 에서 가장 작은수와 가장 큰 수를 뽑아서 곱한다.
# 정렬
def solution(A,B):
    answer = 0
    A.sort(reverse = True)
    B.sort()
    for i in range(len(A)):
        answer += A[i] * B[i]
    
    return answer