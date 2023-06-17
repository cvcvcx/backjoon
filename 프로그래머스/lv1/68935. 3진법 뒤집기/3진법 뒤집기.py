def solution(n):
    answer = 0
    three_str = ""
    while n>0:
        three_str += str(n%3)
        n = n//3
    
    return int(three_str,3)