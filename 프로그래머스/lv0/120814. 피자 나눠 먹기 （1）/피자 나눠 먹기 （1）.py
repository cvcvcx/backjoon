def solution(n):
    piece = 7
    answer = int(n/piece+1) if n % piece != 0 else int(n/piece)
    return answer