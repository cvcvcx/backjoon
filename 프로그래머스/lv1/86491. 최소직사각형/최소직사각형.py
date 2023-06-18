def solution(sizes):
    answer = 0
    x = []
    y = []
    for s in sizes:
        s.sort()
        x.append(s[0])
        y.append(s[1])
    answer = max(x) * max(y)
    return answer