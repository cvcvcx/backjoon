def solution(arr):
    stk = []
    for i in range(len(arr)):
        if len(stk)<1:
            stk.append(arr[i])
        else:
            if stk[-1] == arr[i]:
                stk.pop()
            elif stk[-1] != arr[i]:
                stk.append(arr[i])
    return stk if not len(stk) == 0 else [-1]