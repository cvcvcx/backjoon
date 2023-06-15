def solution(n):
    number_set = set(range(2,n+1))
    for i in range(2,n+1):
        number_set -= set(range(i*2,n+1,i))
    return len(number_set)
    