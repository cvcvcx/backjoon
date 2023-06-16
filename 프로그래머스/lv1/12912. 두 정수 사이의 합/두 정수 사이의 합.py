def solution(a, b):
    answer = 0
    if a == b:
        return a
    elif a > b:
        a, b = b, a
    num_list = list(range(a,b+1))
    answer = sum(num_list)
    return answer