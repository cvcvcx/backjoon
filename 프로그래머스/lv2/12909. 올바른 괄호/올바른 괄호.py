def solution(s):
    answer = True
    stack = []
    for str in s:
        if str == "(":
            stack.append(")")
        else:
            if stack:
                stack.pop()
            else:
                answer = False
    if stack:
        answer = False
    return answer