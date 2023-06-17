def solution(arr):
    stack = []
    for num in arr:
        if len(stack) == 0:
            stack.append(num)
        if len(stack)>0 and stack[-1] != num:
            stack.append(num)
    return stack