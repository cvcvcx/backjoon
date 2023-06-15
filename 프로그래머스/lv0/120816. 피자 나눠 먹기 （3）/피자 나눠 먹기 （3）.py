def solution(slice, n):
    answer = int(n/slice) if n%slice==0 else int(n/slice+1)
    return answer