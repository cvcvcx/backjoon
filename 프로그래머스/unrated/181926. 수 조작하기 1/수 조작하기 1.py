def solution(n, control):
    answer = 0
    c_list = list(control)
    for c in c_list:
        if c == "w":
            n += 1
        elif c == "s":
            n -= 1
        elif c == "d":
            n += 10
        elif c == "a":
            n -= 10
    answer = n
    return answer