import math
def solution(n):
    answer = 0
    piece = 7
    answer = math.ceil(n/piece)
    return answer