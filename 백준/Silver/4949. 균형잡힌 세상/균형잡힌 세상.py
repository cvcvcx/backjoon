while True:
    sentence = input()
    if sentence == ".":
        break
    stack = []
    for s in sentence:
        if s == "(" or s == "[":
            stack.append(s)
        elif s == ")":
            if stack and stack[-1] != "(":
                stack.append(s)
                break
            elif stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(s)
                break
        elif s == "]":
            if stack and stack[-1] != "[":
                stack.append(s)
                break
            elif stack and stack[-1] == "[":
                stack.pop()
            else:
                stack.append(s)
                break
        elif s == ".":
            break
    if not stack:
        print("yes")
    else:
        print("no")
